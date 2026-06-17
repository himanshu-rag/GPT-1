import os

educational_text = """
================================================================================
CHAPTER 1: INTRODUCTION TO COMPUTER NETWORK MODELS
================================================================================

In computer networking, network models are conceptual frameworks that standardize how
data is transmitted over a communications network. They divide the complex process of
network communication into discrete, manageable layers.

There are two primary models used today:
1. The Open Systems Interconnection (OSI) Model (7 Layers)
2. The Transmission Control Protocol / Internet Protocol (TCP/IP) Model (4 Layers)

--------------------------------------------------------------------------------
SECTION 1.1: THE OSI MODEL (7 LAYERS)
--------------------------------------------------------------------------------

The OSI model is a theoretical, logical framework created by the International Organization
for Standardization (ISO). It is composed of seven distinct layers, structured from the
top (user-facing applications) to the bottom (physical wires).

LAYER 7: THE APPLICATION LAYER
- Purpose: Direct interface for user applications to access network services.
- Protocols: HTTP, HTTPS, DNS, SMTP, FTP, SSH, Telnet, DHCP, SNMP.
- Function: Resolves resource availability, identifies communication partners, and
  synchronizes communication. For example, web browsers use HTTP to request webpages.

LAYER 6: THE PRESENTATION LAYER
- Purpose: Acts as a translator, ensuring data is in a readable format for Layer 7.
- Functions: Data translation, formatting, encryption/decryption (such as SSL/TLS),
  and compression (like ZIP or JPEG).
- Example: Converting ASCII code to EBCDIC, or encrypting traffic before transmission.

LAYER 5: THE SESSION LAYER
- Purpose: Establishes, manages, and terminates connections (sessions) between local
  and remote applications.
- Functions: Session checkpointing, recovery, and synchronization.
- Protocols: NetBIOS, RPC (Remote Procedure Call), PPTP.

LAYER 4: THE TRANSPORT LAYER
- Purpose: Handles host-to-host communication, end-to-end data delivery, and reliability.
- Protocols: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- Functions: Segmentation (chopping data into segments), flow control (preventing sender
  from overwhelming receiver), error control (retransmitting lost data), and port
  addressing (identifying target applications like port 80 for HTTP).

LAYER 3: THE NETWORK LAYER
- Purpose: Handles logical routing of packets across different physical networks.
- Protocols: IP (Internet Protocol - IPv4 and IPv6), ICMP (Internet Control Message
  Protocol), IPsec, IGMP.
- Hardware: Routers operate at this layer.
- Functions: Logical addressing (IP addresses) and path determination (routing).

LAYER 2: THE DATA LINK LAYER
- Purpose: Prepares data for transmission over physical media and controls access.
- Protocols: Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), PPP, Frame Relay, ARP.
- Hardware: Switches and network interface cards (NICs) operate at this layer.
- Functions: Physical addressing (MAC addresses), framing (putting packets into frames),
  error detection (using CRC codes), and Media Access Control.

LAYER 1: THE PHYSICAL LAYER
- Purpose: Responsible for the physical transmission of unstructured raw bitstreams
  over a physical medium.
- Media: Fiber-optic cables, coaxial cables, twisted-pair copper cables, radio waves.
- Hardware: Hubs, repeaters, cables, connectors (like RJ-45).
- Function: Converts digital bits (0s and 1s) into electrical, light, or radio signals.

--------------------------------------------------------------------------------
SECTION 1.2: THE TCP/IP MODEL (4 LAYERS)
--------------------------------------------------------------------------------

The TCP/IP model, also known as the Department of Defense (DoD) model, is the practical,
real-world framework that powers the modern Internet. It groups functions into four layers:

1. APPLICATION LAYER (Corresponds to OSI Layers 5, 6, 7)
   - Interfaces directly with application software and handles formatting and sessions.
   
2. TRANSPORT LAYER (Corresponds to OSI Layer 4)
   - Handles host-to-host transport using TCP (reliable) or UDP (fast/unreliable).

3. INTERNET LAYER (Corresponds to OSI Layer 3)
   - Handles logical routing of packets using IP addresses.

4. NETWORK ACCESS LAYER (Corresponds to OSI Layers 1, 2)
   - Handles physical connections, framing data into MAC addresses, and physical signals.

================================================================================
CHAPTER 2: DATA ENCAPSULATION AND DECAPSULATION
================================================================================

Encapsulation is the process where protocol information (headers and footers) is added
to data as it moves down the network stack from the application layer to the physical layer.

1. DATA (Application Layer): The raw payload, e.g., HTTP request header and body.
2. SEGMENT (Transport Layer): TCP adds source and destination port numbers.
3. PACKET (Network Layer): IP adds source and destination IP addresses.
4. FRAME (Data Link Layer): Ethernet adds source and destination MAC addresses and a CRC footer.
5. BITS (Physical Layer): The frame is converted to electrical/optical signals.

Decapsulation is the reverse process, occurring at the receiving device. As the bitstream
is received, the MAC frame header is analyzed and stripped, then the IP packet header,
then the TCP segment header, leaving the raw application data for the application.

================================================================================
CHAPTER 3: CORE NETWORK PROTOCOLS AND THEIR OPERATION
================================================================================

--------------------------------------------------------------------------------
SECTION 3.1: THE TRANSMISSION CONTROL PROTOCOL (TCP)
--------------------------------------------------------------------------------

TCP is a connection-oriented, reliable transport protocol.

THE THREE-WAY HANDSHAKE:
Before TCP transmits data, it must establish a connection using a 3-step handshake:
1. SYN (Synchronize): Client sends a segment with the SYN flag set and a random sequence number (Seq=X).
2. SYN-ACK (Synchronize-Acknowledge): Server replies with SYN and ACK flags set. It acknowledges the
   client's sequence (Ack=X+1) and sends its own random sequence number (Seq=Y).
3. ACK (Acknowledge): Client sends an ACK segment to acknowledge the server's sequence (Ack=Y+1).

TCP RELIABILITY AND FLOW CONTROL:
- Sequence Numbers: Ensure that packets are reconstructed in the correct order.
- Acknowledgments: Receiver sends ACKs to confirm data delivery. Unacknowledged packets are retransmitted.
- Sliding Window (Window Size): The receiver tells the sender how much data it can buffer, preventing buffer overflows.

--------------------------------------------------------------------------------
SECTION 3.2: THE USER DATAGRAM PROTOCOL (UDP)
--------------------------------------------------------------------------------

UDP is a connectionless, unreliable transport protocol. It does not perform handshakes,
sequence tracking, or flow control.

- Features: Low overhead, fast transmission speed, best-effort delivery.
- Use cases: DNS queries, video streaming, voice calls (VoIP), online video games.
- Header Size: Only 8 bytes, compared to TCP's 20-60 byte header.

--------------------------------------------------------------------------------
SECTION 3.3: THE DOMAIN NAME SYSTEM (DNS)
--------------------------------------------------------------------------------

DNS is the directory service of the Internet. It translates human-friendly domain names
(e.g., www.example.com) into IP addresses (e.g., 93.184.216.34).

DNS RESOLUTION PROCESS:
1. Request: Client queries the Local DNS resolver (typically provided by the ISP).
2. Root Name Server: Local resolver queries a Root server to find the (.com) Top-Level Domain (TLD) server.
3. TLD Server: Local resolver queries the TLD server to find the Authoritative Name Server for (example.com).
4. Authoritative Server: Local resolver queries the Authoritative server to get the exact IP address.
5. Response: Local resolver caches the result and returns the IP address to the client.

--------------------------------------------------------------------------------
SECTION 3.4: THE ADDRESS RESOLUTION PROTOCOL (ARP)
--------------------------------------------------------------------------------

ARP bridges Layer 3 (IP addressing) and Layer 2 (MAC addressing).

- Purpose: Finds the physical MAC address associated with a known logical IP address.
- Operation: The sender broadcasts an ARP Request ("Who has IP 192.168.1.1?"). The owner
  of that IP replies with an ARP Reply unicast ("I have that IP, and my MAC is AA:BB:CC...").
- ARP Table/Cache: Operating systems store IP-to-MAC mappings in local memory to speed up communication.
"""

data_path = "/Users/himanshu_rags/Desktop/GPT-1/input_networking.txt"

# Append the educational text to the existing RFC dataset
with open(data_path, 'a', encoding='utf-8') as f:
    f.write("\n\n" + educational_text)

print("Appended network models and protocols chapter to input_networking.txt")
