# 🎭 cast_prank

A standalone LAN-safe prank module designed for Raspberry Pi and forensic simulation. This tool logs timestamped prank events and optionally triggers sound alerts — perfect for dramatic overlays, boot-time traps, or dashboard integration.

---

## 🔧 Features

- 🧠 Timestamped prank logging with OS, hostname, and prank status
- 🔊 Optional sound trigger via `aplay` (e.g., siren, voice alert, beep)
- 🗂️ Auto-creates `logs/` folder and `prank_log.txt` if missing
- 🛡️ Fully offline — no internet dependencies
- 🧪 Ready for boot-time execution, cron jobs, or Flask integration
- 🎯 Modular design — easy to embed in dashboards or games
- 🧩 Compatible with LAN-only overlays and prank triggers
- 🧼 Copy-paste-safe for GitHub deployment and classroom use
- 🧠 Detects OS type and logs prank context for forensic analysis
- 🧱 Can be extended to trigger GPIO, LED, or screen overlays

---

## 🚀 How to Run

### 🔹 Manual Execution
Run directly from terminal:
```bash
python3 cast_prank.py
```

### 🔹 Boot-Time Execution (Optional)

#### Option 1: `.bashrc` Method
Add this to the end of your `.bashrc` file:
```bash
python3 /path/to/cast_prank.py
```

#### Option 2: systemd Service
Create a service file:
```bash
sudo nano /etc/systemd/system/cast_prank.service
```

Paste this:
```ini
[Unit]
Description=LAN Prank Trigger
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/cast_prank.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable cast_prank
sudo systemctl start cast_prank
```

---

## 📁 Output

Creates:
```
logs/
└── prank_log.txt
```

Each entry includes:
```
[YYYY-MM-DD HH:MM:SS] Hostname: <name> | OS: <type> | Prank Triggered
```

---

## 🧪 Integration Ideas

- 🔐 Trigger on login, SSH access, or Flask route
- 🎮 Embed in prank dashboard with buttons or timers
- 📡 Pair with MAC vendor analysis for targeted pranks
- 🧠 Use with overlays, countdowns, or voice alerts
- 🧱 Extend with GPIO for physical prank effects

---

## 🧰 Requirements

- Python 3
- `aplay` (optional, for sound playback)
- LAN-only environment (recommended for safety)
- Raspberry Pi or Linux device

---

## ✅ Ethical Use

- ✅ Only prank devices you own or have permission to simulate
- ✅ Use in LAN-only labs or classrooms
- ✅ Never deploy on public networks or shared systems

---

## 🎓 Credits

Created by [Mr-A-Hacker](https://github.com/Mr-A-Hacker)  
For LAN-only simulations, forensic overlays, and ethical hacking education
