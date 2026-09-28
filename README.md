
# 🔍 Python Network Port Scanner

A multithreaded network port scanner built using Python.  
This tool detects open TCP ports on a target IP and identifies common services running on them.

---

## 🚀 Features

- Fast multithreaded scanning (ThreadPoolExecutor)
- Detects open ports (1–1024 default range)
- Service name identification (HTTP, SSH, etc.)
- Saves scan results to file
- Simple CLI-based tool

---

## 🛠️ Technologies Used

- Python 3
- socket programming
- concurrent.futures (multithreading)

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
