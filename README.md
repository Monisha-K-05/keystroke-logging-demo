# Keystroke Logging Demonstration

This project demonstrates a basic keystroke logging mechanism implemented in Python as part of a cybersecurity internship. The purpose of this project is to understand how keystroke monitoring works and to study the potential security risks associated with such techniques.

## Project Overview
The application captures keyboard input during an active user session and stores the data in both text and JSON formats.  
The program runs in the foreground and requires manual start and stop through a graphical user interface, ensuring ethical and controlled execution.

## Technologies Used
- Python
- pynput library
- tkinter (GUI)
- JSON and text-based logging

## How to Run

1. Install the required dependency:
```bash
pip install pynput
Run the program:

bash
Copy code
python keystroke_logger_gui.py
Use the GUI buttons to start and stop logging.

Output Files
keylog.txt – Stores keystrokes in readable text format

keylog.json – Stores keystrokes in structured JSON format

#Ethical Disclaimer

This project is developed strictly for educational purposes as part of a cybersecurity internship.
It is intended to demonstrate how keystroke logging works in a controlled environment.

The program runs only with user knowledge and consent

It does not run in the background or automatically

It is not intended for malicious use

The author does not encourage or support unethical or illegal activities.