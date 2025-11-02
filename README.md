# 🎭 cast_prank

A standalone LAN-safe prank module designed for Raspberry Pi and forensic simulation. This tool logs timestamped prank events and optionally triggers sound alerts — perfect for dramatic overlays, boot-time traps, or dashboard integration.

---

## 🔧 Features

- 🧠 Timestamped prank logging with OS and hostname
- 🔊 Optional sound trigger via `aplay`
- 🗂️ Auto-creates `logs/` folder and `prank_log.txt`
- 🛡️ Fully offline — no internet dependencies
- 🧪 Ready for boot-time execution or Flask integration

---

## 🚀 Usage

```bash
python3 cast_prank.py
