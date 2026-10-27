# Module 0.4: Networking (weeks 6-9)

Every attack and every defense crosses a network. This module takes four weeks because networking is the single most leveraged foundation in security, and because it reinforces the degree's networking course ([degree-connections.md](../../degree-connections.md)).

**Main resources:** [Professor Messer Network+ N10-009](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) (free videos), [Computer Networking: Principles, Protocols and Practice](https://github.com/CNP3/ebook) (free book, "CNP3"), [High Performance Browser Networking](https://hpbn.co/) (free, "HPBN"), [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/).

**Environment:** your host plus the lab VMs, Wireshark installed on the host.

## Week 6: Models, addressing and the link layer

**Goal:** place any protocol in the OSI and TCP/IP models, and subnet IPv4 fluently.

**R. Read and study (75 min)**
- Professor Messer N10-009: the "Networking Concepts" OSI model videos and the "Network Implementations" addressing videos.
- CNP3: the introduction and the part on the physical and datalink layers (framing, MAC addresses, switching, ARP).
- Notes: the seven OSI layers with one protocol each; MAC vs IP; what a switch, a router and a default gateway do; what ARP is and why it is trust-based.
- Flashcards: OSI layers in order, private address ranges (RFC 1918), CIDR to mask conversions, broadcast vs unicast vs multicast.

**P. Guided practice (90 min)**
- Subnetting drills: 20 problems by hand. Given a network and a prefix, give network address, broadcast, first and last usable host, and host count. Split a /24 into /26, /27 and /28.
- Capture an ARP exchange in Wireshark (clear your ARP cache, then ping a lab host). Identify the request and reply.

**D. Deep practice (3 h)**
- Design the addressing for your home lab: assign each segment (`labnet`, `corpnet`, `malnet`) a subnet, list every host with its IP, and draw the diagram (extend the one in [homelab](../../homelab/README.md)).
- Capture and annotate a full ARP request/reply and explain, in your notes, how ARP spoofing abuses the lack of authentication and what a defender would see.

**E. English (60 min)**
- Read [RFC 826 (ARP)](https://www.rfc-editor.org/rfc/rfc826) section 1 (motivation). Summarize the problem ARP solves in 3 sentences.

**Check yourself**
1. At which OSI layer does a switch operate, and at which a router?
2. Split 192.168.10.0/24 into four equal subnets. Give each one's range.
3. What does ARP map to what, and why can it be spoofed?
4. What is the broadcast address of 10.0.5.0/26?
5. Why is a MAC address not routable across the internet?

**Deliverable:** 20 solved subnetting problems and your lab addressing plan with diagram.

## Week 7: IP, TCP, UDP and routing

**Goal:** explain how data gets from one host to another and read a TCP conversation.

**R. Read and study (75 min)**
- Professor Messer: transport-layer and routing videos (ports, TCP, UDP, common ports).
- HPBN: "Building Blocks of TCP" (the whole chapter).
- Notes: the TCP three-way handshake and teardown; sequence and acknowledgement numbers; TCP flags (SYN, ACK, FIN, RST, PSH); why TCP is reliable and UDP is not; the top 20 ports and their services.
- Flashcards: handshake steps, each TCP flag's meaning, TCP vs UDP trade-offs, ports 20/21, 22, 25, 53, 80, 443, 445, 3389, 3306.

**P. Guided practice (90 min)**
- In Wireshark, capture and follow a full TCP connection to a lab web server (`python3 -m http.server` on a VM). Identify the handshake, data transfer and teardown; use "Follow TCP Stream".
- Capture a UDP DNS query and compare its simplicity with TCP.

**D. Deep practice (3 h)**
- Write a Python TCP client and server with the standard library (`socket`) that exchange a message, run them across two lab VMs, and capture the traffic. Match each packet in Wireshark to a line in your code.
- Then extend [`port_check.py`](exercises/port_check.py): add a `--timeout` sweep and explain, with captures, why a closed port replies with RST immediately while a filtered port times out.

**E. English (60 min)**
- Read [RFC 9293 (TCP)](https://www.rfc-editor.org/rfc/rfc9293) section 3.4 (establishing a connection). Note the exact words for each handshake step.

**Check yourself**
1. Draw the three-way handshake with the flags set in each packet.
2. What does an RST mean, and when is one sent?
3. Why does DNS usually use UDP, and when does it use TCP?
4. How does a port scanner tell open from closed from filtered?
5. What is the difference between a port and a socket?

**Deliverable:** your socket client/server with annotated capture, and the extended `port_check.py`.

## Week 8: DNS, HTTP and TLS

**Goal:** explain everything that happens when a browser loads an HTTPS page.

**R. Read and study (75 min)**
- HPBN: "Transport Layer Security (TLS)" and "HTTP/1.X" and "HTTP/2" overview.
- [The Illustrated TLS 1.3 Connection](https://tls13.xargs.org/): read the whole walkthrough.
- Notes: DNS resolution (recursive vs authoritative, record types A, AAAA, CNAME, MX, TXT, NS); HTTP methods, status codes and headers; the TLS 1.3 handshake and what it protects; why the certificate chain matters.
- Flashcards: DNS record types, HTTP status code classes, `Host` header, `Strict-Transport-Security`, TLS handshake steps, what SNI is.

**P. Guided practice (90 min)**
- `dig` a domain for A, MX, TXT and NS records; capture one query in Wireshark and read it.
- Capture a TLS 1.3 handshake to a public site. Find the ClientHello, the SNI, the offered cipher suites and the key share. Confirm that the certificate is encrypted (unlike TLS 1.2).
- Extend [`http_headers.py`](exercises/http_headers.py) to print the negotiated TLS version and cipher.

**D. Deep practice (3 h)**
- Write a full page in your notes titled "What happens when I load https://example.com", tracing every step: DNS resolution, TCP handshake, TLS handshake, HTTP request and response, rendering. For each step name the protocol, the port and the OSI layer, and attach one capture as evidence.
- This is a classic interview question. You are building the answer now.

**E. English (60 min)**
- Rehearse the "what happens when I load a URL" explanation out loud for two minutes, following [speaking-practice.md](../../english/speaking-practice.md). Record it and note where you hesitated.

**Check yourself**
1. Walk through DNS resolution from empty cache to answer.
2. What does the SNI field reveal, even over TLS?
3. What does HSTS do and what attack does it prevent?
4. Why is a self-signed certificate rejected by browsers by default?
5. What is the difference between HTTP 301, 302, 401, 403 and 404?

**Deliverable:** the "what happens when I load a URL" document with captures, and the extended `http_headers.py`.

## Week 9: Network security basics and tooling

**Goal:** scan and map a network responsibly, and understand the common network defenses.

**R. Read and study (75 min)**
- Professor Messer: network security concepts (firewalls, VPNs, NAT, VLANs, network segmentation).
- [Nmap reference guide](https://nmap.org/book/man.html) (free): host discovery, port scan types, service and version detection, the `-sC` default scripts.
- Notes: stateful vs stateless firewalls; what NAT does and why it is not security; VLAN segmentation; the difference between an IDS and an IPS.
- Flashcards: `nmap -sS`, `-sV`, `-sC`, `-p-`, `-oN`; SYN scan vs connect scan; what an IDS does vs a firewall.

**P. Guided practice (90 min)**
- Scan your own lab with Nmap: host discovery across a subnet, then a full TCP port scan with service and version detection on one host. Save output with `-oA`.
- Compare an Nmap SYN scan with your own `port_check.py` in Wireshark: why is `-sS` faster and stealthier?

**D. Deep practice (3 h)**
- Configure the OPNsense firewall in your lab (homelab stage 2): block `labnet` from the internet by default, allow only Kali to reach `corpnet`, and log blocked traffic. Test every rule from Kali with Nmap and `curl`, and read the resulting firewall logs.
- Document the before/after: what the scan showed with the firewall open vs closed.

**E. English (60 min)**
- Read the Nmap man page section on scan types. Write a 150-word explanation of the difference between `-sS` and `-sT` for someone who has never scanned.

**Check yourself**
1. What is the difference between a SYN scan and a full-connect scan, and why does it matter?
2. What does a stateful firewall track that a stateless one does not?
3. Why is NAT not a security control on its own?
4. How does network segmentation limit an attacker who already has one host?
5. What is the difference between an IDS and an IPS?

**Deliverable:** your Nmap scan outputs, the OPNsense ruleset with before/after evidence, and the firewall log analysis.

**Stretch:** read the "Firewall/IDS Evasion" section of the Nmap book summary and HPBN's chapter on WebSocket and WebRTC.
