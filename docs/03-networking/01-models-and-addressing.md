# Network models and addressing

> [!TIP]
> **In short:** networks are built in layers, and each layer has its own addresses, its own protocols and its own attacks. Memorize the layer model, the difference between a **MAC address** (local delivery) and an **IP address** (end-to-end delivery), and learn to **subnet by hand** until it takes under a minute. Most local-network attacks (ARP spoofing, rogue DHCP, VLAN hopping) work because Layer 2 trusts whoever speaks first, and most of the defenses are switch features you should know by name.

## The layered models

Two models are used together. The **OSI model** (seven layers) is the vocabulary in textbooks and job interviews. The **TCP/IP model** (four layers) is closer to how the internet is actually built.

| OSI layer | TCP/IP layer | Unit of data | Examples | Address or identifier | Typical devices |
|---|---|---|---|---|---|
| 7 Application | Application | Message | HTTP, DNS, SMTP, SSH | URL, hostname | Proxies, WAFs |
| 6 Presentation | Application | Message | TLS, encoding, compression | | |
| 5 Session | Application | Message | Session management, RPC | | |
| 4 Transport | Transport | Segment / datagram | TCP, UDP, QUIC | **Port** | Stateful firewalls |
| 3 Network | Internet | Packet | IP, ICMP, IPsec | **IP address** | Routers, L3 switches |
| 2 Data link | Link | Frame | Ethernet, Wi-Fi, ARP, VLAN | **MAC address** | Switches, access points |
| 1 Physical | Link | Bits | Copper, fiber, radio | | Cables, hubs, radios |

"Layer 2 switch" or "Layer 7 firewall" tells you which header the device looks at when it makes a decision. When you troubleshoot or attack a network, ask which layer the problem lives in; the answer narrows the tools you need.

**Encapsulation** is how layers cooperate. Each layer wraps the data from the layer above with its own header:

```
Application data
[ TCP header | data ]                                    segment
[ IP header  | TCP header | data ]                       packet
[ Eth header | IP header | TCP header | data | FCS ]     frame
```

A packet capture shows all of these headers at once, which is why Wireshark is the best way to learn the models (see [Traffic analysis and scanning](05-traffic-analysis-and-scanning.md)).

## Layer 2: local delivery

### MAC addresses and frames

A **MAC address** is 48 bits written as six hex pairs (`00:1a:2b:3c:4d:5e`). The first three bytes are the manufacturer's **OUI**, which is useful for identifying device types. MAC addresses are only meaningful on the local link; routers rewrite them at every hop. They can be changed in software, so they are an identifier, not a credential.

An Ethernet frame carries destination MAC, source MAC, an EtherType (for example `0x0800` for IPv4, `0x0806` for ARP, `0x86DD` for IPv6), a payload of up to 1,500 bytes and a checksum.

### Switches, VLANs and ARP

A **switch** learns which MAC address lives behind which port (the CAM table) and forwards frames only where needed. A **VLAN** (802.1Q) splits one physical switch into several logical networks by tagging frames; a **trunk** port carries several VLANs between switches. Hosts in different VLANs communicate only through a router or Layer 3 switch, which is where firewall rules apply.

**ARP** answers "which MAC address has this IP address?". The host broadcasts a request, and the owner replies. Nothing authenticates the reply, and hosts accept unsolicited ("gratuitous") ARP replies and cache them.

### Layer 2 attacks and their defenses

| Attack | How it works | Defense (switch feature) |
|---|---|---|
| **ARP spoofing** | The attacker sends false ARP replies so traffic for another host (often the gateway) flows through the attacker | Dynamic ARP Inspection; static entries for critical hosts; encryption end to end |
| **MAC flooding** | Overflow the CAM table so the switch floods frames to every port, enabling sniffing | Port security (limit MACs per port) |
| **Rogue DHCP server** | A malicious host answers DHCP requests with its own gateway or DNS | DHCP snooping (trust only uplinks) |
| **VLAN hopping** | Trick a switch into trunking, or send double-tagged frames to reach another VLAN | Disable DTP; set access ports explicitly; do not use the native VLAN for user traffic |
| **Spanning tree manipulation** | Send crafted BPDUs to become the root bridge and capture traffic | BPDU guard, root guard |
| **Unauthorized device** | Plug into an open port | 802.1X port-based authentication; disable unused ports |

**Practical implication:** do not treat the local network as trusted. Use TLS and authenticated protocols even internally, and enable the switch protections above where you control the switches.

## Layer 3: IP addressing

### IPv4

An IPv4 address is 32 bits, written as four decimal bytes. A **prefix length** (`/24`) states how many leading bits identify the network; the rest identify the host. The same information appears as a dotted **subnet mask** (`255.255.255.0`).

Special ranges to know by heart:

| Range | Purpose |
|---|---|
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | **Private** space (RFC 1918); not routed on the internet |
| `100.64.0.0/10` | Carrier-grade NAT (RFC 6598) |
| `127.0.0.0/8` | Loopback |
| `169.254.0.0/16` | Link-local (self-assigned when DHCP fails) |
| `224.0.0.0/4` | Multicast |
| `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` | Reserved for documentation and examples (RFC 5737); this handbook uses them for sample data |
| `0.0.0.0/0` | "Any address": the default route |

### Subnetting by hand

The method that scales: find the **block size** in the interesting octet, then count.

1. Write the prefix as a mask. Find the octet where the mask is neither 255 nor 0.
2. **Block size = 256 − (mask value in that octet).**
3. The **network address** is the largest multiple of the block size that is less than or equal to the host's value in that octet.
4. The **broadcast address** is the next network address minus one.
5. Usable hosts are everything between them: **2^(host bits) − 2**.

| Prefix | Mask | Block size | Total addresses | Usable hosts |
|---|---|---|---|---|
| /24 | 255.255.255.0 | 256 (last octet) | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 4 | 2 |
| /31 | 255.255.255.254 | 2 | 2 | 2 (point to point, RFC 3021) |

**Worked example.** What are the network, broadcast and range for `10.14.37.200/27`?

- /27 means mask `255.255.255.224`; the interesting octet is the fourth; block size = 256 − 224 = 32.
- Multiples of 32: 0, 32, 64, 96, 128, 160, **192**, 224. The largest ≤ 200 is 192.
- Network `10.14.37.192`, broadcast `10.14.37.223` (224 − 1), usable `10.14.37.193` to `10.14.37.222` (30 hosts).

Verify in Python:

```python
import ipaddress
n = ipaddress.ip_network("10.14.37.200/27", strict=False)
print(n.network_address, n.broadcast_address, n.num_addresses - 2)
```

**Same subnet?** Two hosts can talk directly only if they are in the same network. Apply the prefix to both addresses; if the network addresses match, they are local, otherwise traffic goes through the gateway.

### Drill set

Try each by hand, then check against the answers.

1. `192.168.1.130/26`: network, broadcast, usable range.
2. `10.0.5.77/28`: network, broadcast.
3. `172.16.45.200/21`: network, broadcast.
4. `192.168.100.5/30`: network, broadcast, usable hosts.
5. How many /27 subnets fit in a /24, and how many hosts does each hold?
6. `203.0.113.99/25`: network and broadcast.
7. Are `10.1.1.250/23` and `10.1.2.5/23` in the same subnet?
8. Smallest prefix that holds 500 hosts?
9. Dotted-decimal mask for /20?
10. Range covered by `192.168.0.0/22`?

<details>
<summary>Answers</summary>

1. Block 64; 130 falls in 128-191. Network `192.168.1.128`, broadcast `192.168.1.191`, usable `.129` to `.190` (62 hosts).
2. Block 16; 77 falls in 64-79. Network `10.0.5.64`, broadcast `10.0.5.79`.
3. Mask `255.255.248.0`, block 8 in the third octet; 45 falls in 40-47. Network `172.16.40.0`, broadcast `172.16.47.255`.
4. Block 4; 5 falls in 4-7. Network `192.168.100.4`, broadcast `192.168.100.7`, 2 usable hosts (`.5`, `.6`).
5. Eight subnets (`.0`, `.32`, ... `.224`), each with 30 usable hosts.
6. Block 128; 99 is in 0-127. Network `203.0.113.0`, broadcast `203.0.113.127`.
7. No. A /23 has a block size of 2 in the third octet: `10.1.1.250` is in `10.1.0.0/23`, and `10.1.2.5` is in `10.1.2.0/23`.
8. 500 hosts need at least 502 addresses; 2^9 = 512, so 9 host bits, which is a /23 (510 usable).
9. `255.255.240.0`.
10. `192.168.0.0` to `192.168.3.255` (block size 4 in the third octet).

</details>

### NAT

**Network address translation** lets many private hosts share a public address. The usual form (PAT or "masquerading") rewrites source IP and port on the way out and keeps a table to map replies back. NAT is not a firewall: it blocks unsolicited inbound connections as a side effect, but it provides no policy, and port forwards, UPnP and outbound-initiated connections (the case that matters for malware) all pass through it. With carrier-grade NAT, many customers share one public IP, which complicates attribution and port forwarding.

### DHCP

DHCP assigns addresses automatically through four messages, remembered as **DORA**: Discover (broadcast by the client), Offer, Request, Acknowledge. It uses UDP ports 67 (server) and 68 (client). Because the first message is a broadcast and the first reply wins, a rogue server can hand out a malicious gateway or DNS server, and an attacker can exhaust the address pool by requesting leases with fake MACs. DHCP snooping is the standard control.

### IPv6

IPv6 uses 128-bit addresses written in hex, with `::` standing for one run of zero groups (`2001:db8::1`).

| Prefix | Type |
|---|---|
| `2000::/3` | Global unicast (routable) |
| `fe80::/10` | Link-local (present on every interface) |
| `fc00::/7` | Unique local (private) |
| `ff00::/8` | Multicast |
| `::1` | Loopback |

IPv6 has no broadcast and no ARP: **Neighbor Discovery** (ICMPv6) resolves addresses and **router advertisements** let hosts configure themselves (SLAAC). The security lessons:

- Many networks run IPv6 by default without monitoring or filtering it, creating a blind spot where IPv4 controls do not apply. Either manage IPv6 or disable it deliberately.
- An attacker on the local link can send rogue router advertisements to become the gateway, or answer DHCPv6 requests (the "mitm6" technique). **RA Guard** and DHCPv6 snooping are the defenses.
- Firewall rules must be written for both address families.

## Routing in one paragraph

A host sends traffic for its own subnet directly and everything else to its **default gateway**. Routers use a **routing table** to pick the next hop by the longest matching prefix. Inside an organization, routes are learned with protocols such as OSPF; between organizations, the internet uses BGP, which trusts what neighbors announce. A mistaken or malicious announcement can divert traffic for a whole network, as in the 2008 incident in which a Pakistani ISP's attempt to block YouTube spread to the world. RPKI route-origin validation is the main mitigation (see [TCP, UDP and routing](02-tcp-udp-and-routing.md)).

## Useful commands

```bash
ip -br a                 # interfaces and addresses
ip route                 # routing table and default gateway
ip neigh                 # ARP / neighbor cache
arp -a                   # (legacy) ARP table
ipcalc 10.14.37.200/27   # subnet calculator, if installed
```

```powershell
Get-NetIPConfiguration
Get-NetNeighbor
route print
```

## What to do with this

- [ ] Memorize the OSI layers and name one protocol, one device and one attack for each of layers 2, 3 and 4.
- [ ] Complete the drill set by hand, then 20 more using random addresses and check them with Python.
- [ ] Capture an ARP request and reply in Wireshark and identify every field.
- [ ] In your lab, perform ARP spoofing between two of your own VMs, observe it in a capture, then enable the defense on the virtual switch or host and see it fail.
- [ ] Do [Module 0.4, weeks 6 to 9](../../roadmap/phase-0-foundations/04-networking.md) of the roadmap.

## Key references

Bellovin (1989) · RFC 826 · RFC 1918 · RFC 3021 · RFC 4291 · RFC 4632 · RFC 5737 · RFC 6598 · RFC 8200. Full list in [References](../15-references.md).

<!-- navigation -->
[← Memory, corruption bugs and exploit mitigations](../02-systems/04-memory-and-exploit-mitigations.md) · [Index](../00-start-here.md) · [TCP, UDP, ICMP and routing →](02-tcp-udp-and-routing.md)
