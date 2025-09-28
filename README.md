### Voice LED Control on Raspberry Pi

This project lets you control an LED with your voice commands using a Raspberry Pi.
You can say "turn on" or "turn off" and the LED will switch.
---

## Requirements
- Raspberry Pi with Python 3
- USB Microphone
- One LED + Resistor
- Internet connection (for Google Speech Recognition)
  
---

## Setup

# 1. Install required packages on Raspberry Pi:
- sudo apt update
- sudo apt install python3-pyaudio python3-rpi.gpio
- pip install SpeechRecognition --break-system-packages

# 2. Connect LED
- Use Board pin 11 for LED (through a resistor).
- Connect GND to Board pin 6.

# 3. Check microphone
- arecord -l
In the code, set the right device_index for your mic.

---
## Run the Code
1. Save the script as voice_led.py.
2. Run:
- python3 voice_led.py
- Say "turn on" → LED ON
- Say "turn off" → LED OFF

--- 

## Notes
- Works best in quiet room.
- Press Ctrl + C to stop program.
