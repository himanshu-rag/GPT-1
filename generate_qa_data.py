import random

# A comprehensive list of networking questions and their detailed answers
qa_pairs = [
    {
        "q": "what is my ip",
        "a": "Your IP (Internet Protocol) address is a unique identifier for your device on a network. Local IPs are typically in the range of 192.168.x.x, while public IPs are assigned by your ISP to connect you to the wider internet."
    },
    {
        "q": "what is tcp",
        "a": "TCP (Transmission Control Protocol) is a reliable, connection-oriented transport protocol. It uses a three-way handshake (SYN, SYN-ACK, ACK) to establish a connection and guarantees that packets are delivered in order without errors."
    },
    {
        "q": "what is udp",
        "a": "UDP (User Datagram Protocol) is a connectionless, lightweight transport protocol. It does not perform handshakes or guarantee delivery, making it much faster than TCP and ideal for gaming, streaming, and DNS queries."
    },
    {
        "q": "how does dns work",
        "a": "DNS (Domain Name System) translates human-readable domain names like google.com into numerical IP addresses. It queries root, TLD, and authoritative servers to resolve the domain so your browser can load the site."
    },
    {
        "q": "what is the osi model",
        "a": "The OSI model is a 7-layer theoretical framework for understanding network communications. The layers are Physical, Data Link, Network, Transport, Session, Presentation, and Application."
    },
    {
        "q": "what is a router",
        "a": "A router is a Layer 3 network hardware device that routes data packets between different networks using logical IP addresses to determine the most efficient path."
    },
    {
        "q": "what is a switch",
        "a": "A switch is a Layer 2 network device that connects devices within the same local area network (LAN) and routes data frames directly to their destination using physical MAC addresses."
    },
    {
        "q": "what is a mac address",
        "a": "A MAC (Media Access Control) address is a permanent, 12-character physical hardware address burned into a device's network card (NIC) at the factory."
    },
    {
        "q": "what is a port",
        "a": "A port is a logical endpoint for communication at the Transport Layer. Common examples include Port 80 for HTTP, Port 443 for HTTPS, Port 22 for SSH, and Port 53 for DNS."
    },
    {
        "q": "what is a firewall",
        "a": "A firewall is a network security device that monitors and filters incoming and outgoing network traffic based on an organization's established security rules."
    },
    {
        "q": "what is dhcp",
        "a": "DHCP (Dynamic Host Configuration Protocol) is an application layer protocol that automatically assigns IP addresses, subnet masks, and default gateways to devices on a network."
    },
    {
        "q": "what is ping",
        "a": "Ping is a utility command used to test if a host is reachable. It sends ICMP Echo Request packets and waits for an Echo Reply, measuring the round-trip latency."
    },
    {
        "q": "what is nat",
        "a": "NAT (Network Address Translation) is a method used by routers to translate private local IP addresses into a single public IP address, conserving IP space and adding security."
    },
    {
        "q": "what is an ip address",
        "a": "An IP address is a logical numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication (e.g. IPv4 or IPv6)."
    }
]

# We will generate a larger training file by repeating and formatting the Q&A pairs
# to help the character-level model memorize and generalise the question-answer structure.
def generate_dataset():
    output_path = "input_qa.txt"
    dataset_content = ""
    
    # Repeat the Q&A pairs to build a solid corpus of structured text
    for _ in range(150):
        random.shuffle(qa_pairs)
        for pair in qa_pairs:
            dataset_content += f"Question: {pair['q']}\nAnswer: {pair['a']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset generated! Structured Q&A text written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
