# PRODIGY_CS_04
# Keylogger (Python – Educational Use Only)

This project was developed as part of my internship at **Prodigy InfoTech** for the role of **Cyber Security Intern**.  
The objective was to build a simple **keylogger** using Python to understand how keylogging tools function and to raise awareness about their ethical and legal use.

---

## Description

This keylogger captures and logs keystrokes from the user's keyboard and writes them to a local file. It demonstrates how keyboard input can be monitored using Python's `pynput` library.

---

## Features

- Captures all keystrokes (letters, numbers, special characters, and function keys)
- Logs data to a text file (`keylog.txt`)
- Uses `pynput` for monitoring key events
- Stops safely when the `Esc` key is pressed

---

## Important Notice

> This tool is intended **strictly for educational and ethical purposes**.  
> Use only on systems you own or have **explicit permission** to monitor.  
> Unauthorized use is illegal and unethical.

---

## Requirements

- Python 3.x
- `pynput` module

### Installation

Install the required module:
```bash
pip install pynput

keylogger.py     # Main keylogger script
keylog.txt       # Output file storing the logged keystrokes
README.md        # Project documentation
