# Network Config Backup Tool

Automated Cisco IOS configuration backup tool built with Python and Netmiko.
Connects to multiple network devices, pulls running configs, and saves them
to organized dated folders with full error handling and logging.

## Features
- Backs up running config from multiple Cisco IOS devices simultaneously
- Saves configs to auto-created dated folders
- Handles unreachable devices (timeout)
- Handles wrong credentials (authentication error)
- Generates a log file for every backup session
- Clean summary report — success/failed count

## Tech Stack
- Python 3.x
- Netmiko 4.x
- Cisco IOS (tested on EVE-NG lab)

## Project Structure
```
network-config-backup-tool/
│
├── backup_tool.py          # Main backup script
├── devices.py              # Device list
├── requirements.txt        # Dependencies
├── README.md               # This file
│
└── backups/
    └── 2026-04-22/
        ├── config_192.168.138.130.txt
        ├── config_192.168.138.135.txt
        ├── config_192.168.138.136.txt
        └── backup_log.txt
```


## How It Works
1. Loads device list from `devices.py`
2. Connects to each device via SSH using Netmiko
3. Enters enable mode
4. Pulls running configuration
5. Saves config to dated folder
6. Logs result — success or failure
7. Prints summary report

## Usage

### Install dependencies
```bash
pip install netmiko
```

### Configure devices
Edit `devices.py` and add your devices:
```python
DEVICES = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "cisco123",
        "secret": "cisco123",
    },
]
```

### Run the tool
```bash
python backup_tool.py
```

### Output
```
=============================================
       NETWORK CONFIG BACKUP TOOL
=============================================
  ✅ 192.168.138.130 — backed up
  ✅ 192.168.138.135 — backed up
  ✅ 192.168.138.136 — backed up
  ❕ 192.168.1.99    — unreachable (timeout)
=============================================
  Success : 3
  Failed  : 1
  Folder  : backups/2026-04-22
=============================================
```

## Author
- Name: Rehan
- LinkedIn: https://www.linkedin.com/in/d-rehan/
- GitHub: https://github.com/DilipRehan

## License
MIT
