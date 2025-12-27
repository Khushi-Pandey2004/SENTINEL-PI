# 🔴 SENTINEL PI 🛡️

SENTINEL PI is an end-to-end **Raspberry Pi–based security and monitoring system**, built and documented from **OS installation to secure remote access and deployment**.

This project focuses on real-world setup, debugging, and reproducibility rather than just theory.

---

## 📌 Project Overview

SENTINEL PI was built as a hands-on security system using Raspberry Pi, where the entire process — from flashing the OS to running security tools and monitoring — is implemented, tested, and documented.

The project reflects real challenges faced during system setup, networking, and security tool integration.

---

## ⚙️ Features

- Raspberry Pi OS installation and configuration  
- Secure SSH-based remote access  
- Python-based implementation  
- Network monitoring using Suricata  
- Security monitoring using Wazuh  
- Real-time logs and alerts  
- Fully documented setup with screenshots and demo video  

---

## 🛠️ Tech Stack

### Hardware
- Raspberry Pi (specify model)
- SD Card (minimum 16GB)
- Power Supply

### Software
- Raspberry Pi OS (32-bit / 64-bit)
- Python 3
- SSH
- Suricata
- Wazuh
- Linux utilities

---

## 🚀 Setup & Installation

### 1️⃣ Flash Raspberry Pi OS
- Use Raspberry Pi Imager
- Enable SSH during OS setup
- Configure username, password, Wi-Fi, and locale

### 2️⃣ Connect via SSH
bash : 
ssh predator@raspberrypi.local 

### 3️⃣ Update System
sudo apt update && sudo apt upgrade -y

### 4️⃣ Install Dependencies
sudo apt install python3 python3-pip suricata -y

### 5️⃣ Run the Project
python3 ids_alert_monitor_script.py

---

## 📂 Project Structure
```
SENTINEL-PI/
├── code/
│ └── ids_alert_monitor_script.py
├── screenshots/
├── demo-video/
├── report/
│ └── SENTINEL_PI_Project_Report.pdf
└── README.md
```
---

## 📸 Demo & Results

Screenshots of system setup and logs are available in the screenshots/ folder
Working demo video is included in the repository
Detailed technical report explains the complete workflow

---

## 🧠 Challenges & Learnings

Debugging repeated SSH connection failures
Handling Suricata configuration and rule issues
Wazuh Cloud account bans and agent failures
Understanding real-world log flow and live data monitoring
This project significantly improved my understanding of Linux systems, networking, and security monitoring.

---

## 🔮 Future Improvements

Automating agent deployment
Cloud-independent monitoring setup
Alert visualization dashboard
Hardening SSH and system security

---

## 👤 Author

Your Name - Khushi,

Contact/Ask me at khushupandey2004@gmail.com

---
