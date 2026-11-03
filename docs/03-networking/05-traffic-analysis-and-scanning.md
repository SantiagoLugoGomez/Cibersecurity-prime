# Traffic analysis and scanning

> [!TIP]
> **In short:** a packet capture is the ground truth of what happened on a network, and **Wireshark** with **display filters** is the fastest way to read it. **Nmap** is the standard way to learn what a network exposes. Both are dual-use: the same technique that maps your lab can map someone else's, which is a crime without permission. Learn to capture, filter and follow a stream; learn what each scan type sends and what it looks like from the defender's side; and always keep the scope and authorization in writing.

> [!CAUTION]
> Capture only on networks you own or administer, and scan only systems you are authorized to test. Scanning and sniffing other people's networks can violate Ley 1273 de 2009 (see [Legal limits and ethics](../01-foundations/05-legal-and-ethics.md)).

## Capturing traffic

| Tool | Use |
|---|---|
| **Wireshark** | Graphical analyzer; decodes hundreds of protocols |
| **tshark** | Wireshark's command-line version; scriptable |
| **tcpdump** | Lightweight capture, standard on servers |
| **Zeek** | Turns traffic into structured logs (see below) |

A capture needs a place where the traffic passes: the host's own interface, a switch **SPAN/mirror port**, a network **TAP**, or a virtual switch with promiscuous mode in your lab. Encrypted traffic (TLS, SSH, VPN) shows metadata but not content; a capture of HTTPS still tells you who talked to whom, when, how much and with what certificate.

```bash
sudo tcpdump -i eth0 -w capture.pcap                      # write to file
sudo tcpdump -i eth0 -nn 'host 10.10.20.50 and port 445'  # capture filter
tshark -r capture.pcap -q -z conv,tcp                     # conversations
```

Mind the difference between two kinds of filter:

- **Capture filters** (BPF syntax, used by tcpdump and Wireshark's capture dialog) decide what is *recorded*.
- **Display filters** (Wireshark's own syntax) decide what is *shown* from what was recorded. You can change them freely afterwards.

## Reading a capture in Wireshark

A reliable workflow:

1. **Orient.** *Statistics → Conversations* and *Protocol Hierarchy* show who talked and with which protocols.
2. **Narrow.** Apply a display filter to the host or protocol of interest.
3. **Follow.** *Right-click → Follow → TCP Stream* shows the whole exchange in order.
4. **Extract.** *File → Export Objects* saves files transferred over HTTP, SMB and others.
5. **Time.** Look at timing: regular intervals suggest automation, such as malware beaconing.

### Display filters you will use constantly

| Goal | Filter |
|---|---|
| One host | `ip.addr == 10.10.20.50` |
| One conversation | `ip.addr == 10.10.20.50 && ip.addr == 10.10.20.10` |
| A port | `tcp.port == 445` |
| Protocol | `dns`, `http`, `tls`, `smb2`, `kerberos`, `arp` |
| TCP SYNs without ACK (scan or connection attempts) | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| Resets | `tcp.flags.reset == 1` |
| Retransmissions and problems | `tcp.analysis.flags` |
| HTTP requests | `http.request` |
| HTTP responses with errors | `http.response.code >= 400` |
| DNS queries for a name | `dns.qry.name contains "example"` |
| TLS handshakes with the server name | `tls.handshake.type == 1` (then read `tls.handshake.extensions_server_name`) |
| Text anywhere in packets | `frame contains "password"` |

### What common activity looks like

| Activity | Signature in a capture |
|---|---|
| **TCP port scan (SYN)** | One source sending SYNs to many ports on one host, with RSTs from closed ports and SYN+ACKs from open ones |
| **Host sweep** | One source sending ARP requests or ICMP echoes to every address in a range |
| **Brute force** | Many short connections to one service (SSH 22, RDP 3389, SMB 445) with repeated authentication failures |
| **Beaconing** | A host connecting to the same external destination at near-regular intervals with similar sizes |
| **DNS tunneling** | Very long or high-entropy subdomains; many TXT or NULL queries to one domain |
| **Data exfiltration** | A large, one-directional flow to an unusual destination, often after hours |
| **ARP spoofing** | Two IPs claiming the same MAC, or repeated unsolicited ARP replies |
| **Cleartext credentials** | FTP, Telnet, HTTP Basic, POP3 or LDAP simple binds exposing passwords |

Learning from real malicious captures is possible with the public training exercises at malware-traffic-analysis.net, which publishes pcaps with write-ups. Use them in an isolated lab, because the files are the traffic of real infections.

## Zeek and Suricata

Full packet capture is large and slow to search. Two open-source tools turn traffic into something you can query.

| Tool | Approach | Output |
|---|---|---|
| **Zeek** | Passive network security monitor that records what happened | Structured logs per protocol: `conn.log` (every connection), `dns.log`, `http.log`, `ssl.log`, `files.log`, `x509.log` |
| **Suricata** | Signature-based intrusion detection and prevention engine | Alerts (EVE JSON) when traffic matches rules, plus protocol logs |

They are complementary: Suricata says "this matches a known-bad rule", while Zeek lets you ask later "which hosts contacted this domain in the last month?". A shared **Community ID** hash lets you pivot from a Suricata alert to the matching Zeek logs. **Security Onion** bundles both with a search interface and is a good lab project (see [Home lab](../../homelab/README.md)).

## Network scanning with Nmap

Nmap discovers hosts, open ports, services and versions. It is the standard tool for the reconnaissance phase of an authorized test and for auditing your own exposure.

### Scan types

| Option | Technique | What it sends | Notes |
|---|---|---|---|
| `-sS` | **SYN ("half-open") scan** | SYN; reads SYN+ACK or RST; never completes the handshake | Default when run as root; fast; less noisy in application logs |
| `-sT` | **Connect scan** | Full TCP connection through the OS | Used without privileges; leaves entries in service logs |
| `-sU` | **UDP scan** | UDP probes | Slow and ambiguous; essential because many services (DNS, SNMP, NTP) use UDP |
| `-sV` | Service and version detection | Probes open ports for banners | Needed to find vulnerable versions |
| `-sC` | Default scripts (NSE) | Safe scripts for common checks | Equivalent to `--script=default` |
| `-O` | OS detection | TCP/IP stack fingerprinting | Needs at least one open and one closed port |
| `-A` | Aggressive | `-sV -sC -O --traceroute` | Convenient, noisy |
| `-Pn` | Skip host discovery | Treat every host as up | Use when ICMP is blocked |
| `-p-` | All 65,535 TCP ports | | Default scans only the top 1,000 |

Port states reported: **open**, **closed**, **filtered** (no answer or an ICMP block, so a firewall is in the way), **unfiltered**, and the ambiguous **open|filtered** and **closed|filtered**.

### A sensible workflow (lab or authorized target)

```bash
# 1. Which hosts are alive?
nmap -sn 10.10.20.0/24 -oA out/discovery

# 2. All TCP ports on one host, fast
sudo nmap -p- --min-rate 1000 -T4 10.10.20.50 -oA out/all-tcp

# 3. Service and script detail on the open ports only
sudo nmap -sV -sC -p 22,80,445,3389 10.10.20.50 -oA out/detail

# 4. The top UDP ports
sudo nmap -sU --top-ports 50 10.10.20.50 -oA out/udp
```

Always save output (`-oA` writes normal, XML and grepable formats). Record the command, target, time and version of every scan; your report depends on it. Timing templates `-T0` to `-T5` trade speed against noise and reliability; on fragile or monitored systems go slower, and never run aggressive timing against production without agreement.

### Reading results with judgment

- An open port is not a vulnerability. It is an *exposure* to evaluate: what is the service, which version, who needs it?
- Version banners can be wrong or hidden. Confirm before reporting.
- `filtered` often means a firewall is working. Do not call it a finding.
- Compare against what *should* be exposed. The valuable result is usually the unexpected port.

### Scanning as a defender

Run scans of your own estate regularly, from inside and outside, and diff the results against the previous run. Tools such as `ndiff` (bundled with Nmap) highlight changes, and a new open port on a server is an event worth an explanation. Continuous exposure management products automate the same idea.

## Detecting scans

| Indicator | Where |
|---|---|
| One source touching many ports or hosts in a short window | Firewall logs, NetFlow, Zeek `conn.log` (many failed or short connections), Suricata scan rules |
| Many SYNs with few completed handshakes, and bursts of RSTs | Packet capture, flow data |
| Requests to ports that nothing uses | Firewall deny logs on internet-facing hosts |
| Scans from your own network | Even more important: an internal host scanning peers usually means compromise or an unauthorized tool |

Internet-facing hosts are scanned constantly by research and criminal scanners, so external scan alerts are mostly noise. An **internal** scan or a scan followed by a successful login is the one to investigate.

## Practice

1. Capture the traffic of a TCP SYN scan and a connect scan of your lab host in the same Wireshark session, and write down the differences (the connect scan completes handshakes and appears in service logs).
2. Reproduce the filters in the table above on a real capture.
3. Run Zeek over a pcap and answer: which external domains were contacted, and what is the longest connection?
4. Capture an authentication over each of FTP, SSH and HTTPS and note what is visible in each.

These map to [Module 0.4](../../roadmap/phase-0-foundations/04-networking.md) and [Module 1.5](../../roadmap/phase-1-security-fundamentals/05-network-defense-monitoring.md) of the roadmap.

## What to do with this

- [ ] Build a personal cheat sheet of the display filters and Nmap options above.
- [ ] Scan your own lab, save the results and explain every open port.
- [ ] Capture a full web login and find the session cookie in the capture, then repeat over HTTPS and observe what changes.
- [ ] Install Zeek or Security Onion and read a `conn.log` from your own traffic.
- [ ] Write a detection note for "internal host scanning peers", as in the roadmap.

## Key references

Lyon (2009) · Sanders (2017) · RFC 9293 · Wireshark User's Guide · Zeek documentation · Suricata documentation. Full list in [References](../15-references.md).

<!-- navigation -->
[← Network defense architecture](04-network-defense-architecture.md) · [Index](../00-start-here.md) · [Cryptography foundations →](../04-cryptography-and-identity/01-cryptography-foundations.md)
