# Lehigh First-Year Engineering Test-Follow Platform

This codebase serves as a test-follow platform for students participating in Lehigh University first-year engineering projects.  

> ⚠️ **Please use in accordance with university guidelines and community standards.**  
> Free to use and modify for derivative works. Provided *as-is* with no warranty.

---

## Maintainer
- **Name**: Joshua Kraus  
- **Email**: jjk226@lehigh.edu  

---
## 💻 How to Use the Raspbery Pi

1. Insert the provided SD card ad power the Pi using a micro-usb cord.
2. Give the Pi ~25 seconds to boot and connect to lehigh-guest
3. Connect your computer to lehigh-guest to allow connection over this shared network
4. Open Terminal (Mac) or PowerShell (Windows)
5. Initiate a SSH tunnel connection
6. TIP: ssh into the the pi using '''ssh pi@*NAME_OF_THE_KIT*''' and hitting enter
7. The terminal will ask for the Pi's passowrd, which is on the kit
8. Once inside, follow the remaining steps to: pull, source and run the project code/environments

---
## 📥 How to Pull This Repository and use it's code

1. Navigate to the folder where you want this code:  
   ```bash
   # Create and navigate to a storage folder for this project
   mkdir projects
   cd ~/projects
   # Clone this repository to collect its code:
   git clone https://github.com/jjk-star-bash/lehigh_mushroom.git
   # Navigate to the cloned folder
   cd lehigh_mushroom
   # if you see it, congrats you sucsesssfully pulled the repo
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
