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
```bash
pip install smbus2 adafruit-circuitpython-bmp280

IF YOU GET AN ERROR ABOUT GLABAL INSTALL USING PIP, ACTIVATE A VIRTUAL ENVIRONEMNT AND USE PIP THERE!
HOW TO DO THIS:

# Create the env.
python3 -m venv venv

# Source it
source venv/bin/activate

# Install deps.
pip install smbus2 adafruit-circuitpython-bmp280

# When done working exit the env
deactivate

```
---

## Files:

### `raw-test.py`
Reads sensor data from the AHT20 + BMP280 sensor.  
- **Note**: This script bypasses standard sensor libraries and applies Bosch calibration adjustments.  
- **Status**: Incomplete but functional.

---
