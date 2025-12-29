# Keystroke Logging Demonstration

This project demonstrates a **basic keystroke logging mechanism** implemented in Python as part of a **cybersecurity internship**.  
It is intended for **educational purposes only**, to understand how keystroke monitoring works and the potential security risks.

---

## Project Overview

The application captures keyboard input during an active user session and stores the data in **text** and **JSON** formats.  

**Key Features:**
- Runs in the foreground (manual start/stop via GUI)
- Captures keystrokes ethically and in a controlled environment
- Stores logs in both human-readable and structured formats

---

## Technologies Used

- **Python**  
- **pynput** library for keyboard monitoring  
- **tkinter** for GUI  
- **JSON** and **text-based logging**  

---

## How to Run

1. Install the required dependency:
   ```bash
   pip install pynput

2. Run the program:
   ```bash
   python keystroke_logger_gui.py
Use the **GUI buttons** to start and stop logging.

## Output Files

| File Name   | Description                                 |
|-------------|---------------------------------------------|
| keylog.txt  | Stores keystrokes in readable text format   |
| keylog.json | Stores keystrokes in structured JSON format |

## Ethical Disclaimer

This project is developed strictly for **educational purposes** as part of a cybersecurity internship.

- Demonstrates keystroke logging in a **controlled environment**  
- Runs only with **user knowledge and consent**  
- **Does not run in the background automatically**  
- **Not intended for malicious use**  

The author **does not encourage or support unethical or illegal activities**.
## Author

**MONISHA K** – Cybersecurity Intern




