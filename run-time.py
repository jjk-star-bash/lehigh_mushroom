#!/usr/bin/env python

import drivers
import board
import busio
import adafruit_ahtx0
import adafruit_bmp280
from time import sleep

# Initialize I2C and sensors
i2c = busio.I2C(board.SCL, board.SDA)
aht20 = adafruit_ahtx0.AHTx0(i2c)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Initialize LCD
display = drivers.Lcd()

def scroll_text(line1, line2, delay=0.3):
    max_len = max(len(line1), len(line2))
    for i in range(max_len - 15):  # 16x2 display, so window is 16 chars (0-indexed)
        display.lcd_display_string(line1[i:i+16].ljust(16), 1)
        display.lcd_display_string(line2[i:i+16].ljust(16), 2)
        sleep(delay)

try:
    while True:
        # Read sensor values
        temp_aht = aht20.temperature
        humidity = aht20.relative_humidity
        temp_bmp = bmp280.temperature
        pressure = bmp280.pressure

        # Average temperature from both sensors
        temp_avg = (temp_aht + temp_bmp) / 2

        # Format values
        line1 = f"Temp:{temp_avg:.1f}C Hum:{humidity:.1f}%"
        line2 = f"Pres:{pressure:.1f}hPa"

        scroll_text(line1 + "   ", line2 + "   ", delay=0.3)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
