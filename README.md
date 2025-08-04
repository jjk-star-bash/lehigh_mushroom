# Lehigh First-Year Engineering Test-Follow Platform

This codebase serves as a test-follow platform for students participating in Lehigh University first-year engineering projects.  

> ⚠️ **Please use in accordance with university guidelines and community standards.**  
> Free to use and modify for derivative works. Provided *as-is* with no warranty.

---

## Maintainer
- **Name**: Joshua Kraus  
- **Email**: jjk226@lehigh.edu  

---
## 📥 How to Pull This Repository

1. Open a terminal on your Raspberry Pi (or any Linux machine).  
2. Navigate to the folder where you want this code:  
   ```bash
   # Navigate to starage folder or make a new one using mkdir:
   cd ~/projects
   # Clone the repository:
   git clone https://github.com/jjk-star-bash/lehigh_mushroom.git
   # Navigate to the cloned folder
   cd lehigh_mushroom
   ```
   ---

## Dependencies: 
	•	Raspberry Pi OS installed
	•	Python 3 installed
	•	I2C enabled on the Pi (use sudo raspi-config)
	•	Required libraries: smbus2, adafruit-circuitpython-bmp280
 	•	lcd repository clone

## HOW-TO get dependencies: 

```bash
pip install smbus2 adafruit-circuitpython-bmp280

IF YOU GET AN ERROR AT THIS STEP ABOUT GLOBAL INSTALL USING PIP, ACTIVATE A VIRTUAL ENVIRONEMNT AND USE PIP THERE!
HOW TO DO THIS:

# Create the env.
python3 -m venv venv

# Source it
source venv/bin/activate

# Continue To Install deps.
pip install smbus2 adafruit-circuitpython-bmp280
```

```bash
# Next clone the lcd repository (must do this)
git clone https://github.com/the-raspberry-pi-guy/lcd.git
cd lcd/
sudo ./install.sh
# pi will need to reboot
```
---

## Files:

### `raw-test.py`
Reads sensor data from the AHT20 + BMP280 sensor (THIS IS A TEST FILE, RAW DATA WILL BE FED TO TERMINAL).  
- **Note**: This script bypasses standard sensor libraries and applies Bosch calibration adjustments.  
- **Status**: Incomplete but functional.

### `run-time.py`
Reads Temp, Pres, Humidity from the AHT20 + BMP280 sensor and displays to the 16x20 lcd display until quit.  
- **Note**: This script USES standard sensor libraries.  
- **Status**: Functional.


---
