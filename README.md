# 🚀 Linux Sandbox Environment

A secure Linux-based sandbox system to execute untrusted code and commands using Docker containers with resource limitations.

## 🔥 Features
- Multi-language support (Python, C++, Java)
- Linux command execution (sandboxed)
- Docker-based isolation
- CPU & memory limits
- Timeout protection
- Web-based UI

## 🛠 Tech Stack
- Python (Flask)
- Docker
- Linux
- Java / C++
- HTML + JS

## ⚙️ How to Run

```bash
git clone https://github.com/arushrai007/linux-sandbox.git
cd linux-sandbox
docker build -t sandbox-image .
python3 app.py
