# 🕶️ MACChangerX

**MACChangerX** is a simple Python-based tool that allows ethical hackers and cybersecurity students to change the MAC address of a network interface on Linux systems. It is designed for **educational and penetration testing purposes only**.

---

## 🚀 Features

* Change MAC address of any network interface
* Validate network interface existence
* Works on Linux systems (Kali Linux recommended)
* Clean ASCII banner for professional appearance
* Uses native system commands (`ifconfig`)

---

## 🛠️ Requirements

* Linux OS (Tested on Kali Linux)
* Python 3.x
* Root privileges (sudo)

---

## 📦 Installation

```bash
git clone https://github.com/ramad0na/MACChangerX.git
cd MACChangerX
sudo python3 mac.py
```

---

## ▶️ Usage

```bash
sudo python3 mac.py
```

You will be prompted to:

1. Enter the network interface name (e.g. `eth0`, `wlan0`)
2. Enter the new MAC address

Example:

```text
Enter network interface: wlan0
Enter new mac address: 00:11:22:33:44:55
```

---

## 📌 Sample Output

```text
[+] Changing MAC Address for wlan0 to 00:11:22:33:44:55
```

---

## ⚠️ Disclaimer

This tool is intended **strictly for educational purposes and authorized security testing only**.

Any misuse of this tool for illegal activities is **strictly prohibited**. The author takes no responsibility for any damage or misuse.

---

## 🎯 Why This Tool Matters (For CV)

This project demonstrates:

* Understanding of Linux networking
* MAC spoofing concepts
* Python automation
* Secure scripting practices
* Ethical hacking fundamentals


---

## 🔮 Future Improvements

* Automatic MAC generation
* Support for ip link 

---

## 👨‍💻 Author

**Ahmed Ramadan Mohamed**
Information Security Researcher

---

⭐ If you find this project useful, don’t forget to star it on GitHub!
