import random

def generate_dataset():
    protocols = ["TCP", "UDP"]
    normal_states = ["ESTABLISHED", "CLOSED"]
    
    log_templates = []
    
    # 1. Normal Web & DNS Traffic (representing normal UNSW-NB15 / CIC-IDS2017 traffic)
    for _ in range(3000):
        src_ip = f"192.168.1.{random.randint(10, 250)}"
        dst_ip = random.choice(["93.184.216.34", "104.244.42.1", "172.217.16.142"])
        spt = random.randint(49152, 65535)
        dpt = random.choice([80, 443])
        pkts = random.randint(5, 50)
        bytes_sent = pkts * random.randint(100, 1000)
        log = f"proto=TCP src={src_ip} spt={spt} dst={dst_ip} dpt={dpt} packets={pkts} bytes={bytes_sent} state=ESTABLISHED label=NORMAL"
        log_templates.append(log)
        
    for _ in range(1000):
        src_ip = f"192.168.1.{random.randint(10, 250)}"
        dst_ip = "8.8.8.8"
        spt = random.randint(49152, 65535)
        dpt = 53
        pkts = random.randint(1, 4)
        bytes_sent = pkts * random.randint(50, 150)
        log = f"proto=UDP src={src_ip} spt={spt} dst={dst_ip} dpt={dpt} packets={pkts} bytes={bytes_sent} state=NONE label=NORMAL"
        log_templates.append(log)

    # 2. DDoS Attack (representing CIC-DDoS2019 / CIC-IDS2017 DDoS)
    # Characterized by high packet rate, same destination, spoofed random IPs, SYN_SENT state
    for _ in range(2000):
        src_ip = f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
        dst_ip = "192.168.1.1" # victim server
        spt = random.randint(1024, 65535)
        dpt = 80
        log = f"proto=TCP src={src_ip} spt={spt} dst={dst_ip} dpt={dpt} packets=1 bytes=40 state=SYN_SENT label=DDOS_ATTACK"
        log_templates.append(log)

    # 3. Brute Force Attack (representing UNSW-NB15 / NSL-KDD Brute Force SSH)
    # Characterized by many connection attempts to Port 22 from the same external IP
    attacker_ip = "198.51.100.12"
    for _ in range(800):
        spt = random.randint(30000, 60000)
        dst_ip = "192.168.1.20"
        log = f"proto=TCP src={attacker_ip} spt={spt} dst={dst_ip} dpt={22} packets=3 bytes=144 state=CLOSED label=BRUTE_FORCE_SSH"
        log_templates.append(log)

    # 4. Web Attack (representing CIC-IDS2017 Web Attacks, SQL Injection & XSS)
    # Characterized by suspicious query payloads on Port 80/443
    web_attackers = ["198.51.100.55", "203.0.113.99"]
    sql_payloads = [
        "GET /index.php?id=1' OR '1'='1",
        "GET /login.php?user=admin'--",
        "GET /products.php?cat=1; DROP TABLE users;",
        "POST /submit.php?val=<script>alert('XSS')</script>"
    ]
    for _ in range(800):
        src_ip = random.choice(web_attackers)
        dst_ip = "192.168.1.20"
        spt = random.randint(40000, 50000)
        payload = random.choice(sql_payloads)
        log = f"proto=TCP src={src_ip} spt={spt} dst={dst_ip} dpt=80 payload=\"{payload}\" state=ESTABLISHED label=WEB_ATTACK"
        log_templates.append(log)

    # 5. Botnet Activity (representing UNSW-NB15 / CIC-IDS2017 Botnets)
    # Characterized by repeating periodic beacons to C2 server on non-standard ports
    botnet_ips = ["192.168.1.112", "192.168.1.115"]
    c2_server = "198.51.100.44"
    for _ in range(800):
        src_ip = random.choice(botnet_ips)
        spt = random.randint(50000, 55000)
        log = f"proto=TCP src={src_ip} spt={spt} dst={c2_server} dpt=8080 packets=2 bytes=96 state=ESTABLISHED label=BOTNET_BEACON"
        log_templates.append(log)

    # Shuffle the logs to represent a mixed network capture stream (like PCAP or CSV)
    random.shuffle(log_templates)
    
    # Write to dataset file
    output_path = "data/input_ids.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_templates) + "\n")
    print(f"Dataset generated successfully! {len(log_templates)} logs written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
