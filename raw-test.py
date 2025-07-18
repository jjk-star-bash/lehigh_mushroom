from smbus2 import SMBus
import time

# I2C addresses
AHT10_ADDR = 0x38
BME280_ADDR = 0x77

# Initialize I2C bus
bus = SMBus(1)

# --------- AHT10 Functions ---------
def aht10_init():
    # Soft reset
    bus.write_byte(AHT10_ADDR, 0xBA)
    time.sleep(0.02)
    # Initialize (calibrate)
    bus.write_i2c_block_data(AHT10_ADDR, 0xE1, [0x08, 0x00])
    time.sleep(0.02)

def aht10_read():
    # Trigger measurement
    bus.write_i2c_block_data(AHT10_ADDR, 0xAC, [0x33, 0x00])
    time.sleep(0.08)  # Wait for measurement
    data = bus.read_i2c_block_data(AHT10_ADDR, 0x00, 6)

    humidity_raw = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4))
    humidity = humidity_raw * 100 / 1048576

    temperature_raw = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5])
    temperature = (temperature_raw * 200 / 1048576) - 50

    return temperature, humidity

# --------- BME280 Functions ---------
def bme280_init():
    # Soft reset
    bus.write_byte_data(BME280_ADDR, 0xE0, 0xB6)
    time.sleep(0.1)
    # Set oversampling
    bus.write_byte_data(BME280_ADDR, 0xF2, 0x01)  # Humidity oversampling x1
    bus.write_byte_data(BME280_ADDR, 0xF4, 0x27)  # Temp/press oversampling x1, normal mode
    bus.write_byte_data(BME280_ADDR, 0xF5, 0xA0)  # Config
    time.sleep(0.1)

def bme280_read_calibration():
    # Read calibration data
    calib = bus.read_i2c_block_data(BME280_ADDR, 0x88, 26) + bus.read_i2c_block_data(BME280_ADDR, 0xE1, 7)

    dig_T1 = calib[1] << 8 | calib[0]
    dig_T2 = (calib[3] << 8 | calib[2]) if calib[3] < 128 else (calib[3] << 8 | calib[2]) - 65536
    dig_T3 = (calib[5] << 8 | calib[4]) if calib[5] < 128 else (calib[5] << 8 | calib[4]) - 65536

    dig_P1 = calib[7] << 8 | calib[6]
    dig_P2 = (calib[9] << 8 | calib[8]) if calib[9] < 128 else (calib[9] << 8 | calib[8]) - 65536
    dig_P3 = (calib[11] << 8 | calib[10]) if calib[11] < 128 else (calib[11] << 8 | calib[10]) - 65536
    dig_P4 = (calib[13] << 8 | calib[12]) if calib[13] < 128 else (calib[13] << 8 | calib[12]) - 65536
    dig_P5 = (calib[15] << 8 | calib[14]) if calib[15] < 128 else (calib[15] << 8 | calib[14]) - 65536
    dig_P6 = (calib[17] << 8 | calib[16]) if calib[17] < 128 else (calib[17] << 8 | calib[16]) - 65536
    dig_P7 = (calib[19] << 8 | calib[18]) if calib[19] < 128 else (calib[19] << 8 | calib[18]) - 65536
    dig_P8 = (calib[21] << 8 | calib[20]) if calib[21] < 128 else (calib[21] << 8 | calib[20]) - 65536
    dig_P9 = (calib[23] << 8 | calib[22]) if calib[23] < 128 else (calib[23] << 8 | calib[22]) - 65536

    dig_H1 = calib[25]
    dig_H2 = (calib[27] << 8 | calib[26]) if calib[27] < 128 else (calib[27] << 8 | calib[26]) - 65536
    dig_H3 = calib[28]
    dig_H4 = (calib[29] << 4 | (calib[30] & 0x0F))
    dig_H5 = (calib[31] << 4 | (calib[30] >> 4))
    dig_H6 = calib[32] if calib[32] < 128 else calib[32] - 256

    return {
        'T1': dig_T1, 'T2': dig_T2, 'T3': dig_T3,
        'P1': dig_P1, 'P2': dig_P2, 'P3': dig_P3, 'P4': dig_P4, 'P5': dig_P5,
        'P6': dig_P6, 'P7': dig_P7, 'P8': dig_P8, 'P9': dig_P9,
        'H1': dig_H1, 'H2': dig_H2, 'H3': dig_H3, 'H4': dig_H4,
        'H5': dig_H5, 'H6': dig_H6
    }

def bme280_read(calib):
    data = bus.read_i2c_block_data(BME280_ADDR, 0xF7, 8)

    adc_P = ((data[0] << 16) | (data[1] << 8) | data[2]) >> 4
    adc_T = ((data[3] << 16) | (data[4] << 8) | data[5]) >> 4
    adc_H = (data[6] << 8) | data[7]

    # Temperature compensation
    var1 = (((adc_T >> 3) - (calib['T1'] << 1)) * calib['T2']) >> 11
    var2 = (((((adc_T >> 4) - calib['T1']) * ((adc_T >> 4) - calib['T1'])) >> 12) * calib['T3']) >> 14
    t_fine = var1 + var2
    temperature = (t_fine * 5 + 128) >> 8
    temperature = temperature / 100.0

    # Pressure compensation
    var1 = t_fine - 128000
    var2 = var1 * var1 * calib['P6']
    var2 += ((var1 * calib['P5']) << 17)
    var2 += (calib['P4'] << 35)
    var1 = ((var1 * var1 * calib['P3']) >> 8) + ((var1 * calib['P2']) << 12)
    var1 = (((1 << 47) + var1) * calib['P1']) >> 33

    if var1 == 0:
        pressure = 0
    else:
        p = 1048576 - adc_P
        p = (((p << 31) - var2) * 3125) // var1
        var1 = (calib['P9'] * (p >> 13) * (p >> 13)) >> 25
        var2 = (calib['P8'] * p) >> 19
        pressure = ((p + var1 + var2) >> 8) + (calib['P7'] << 4)
        pressure = pressure / 25600.0

    # Humidity compensation
    h = t_fine - 76800
    h = (((((adc_H << 14) - (calib['H4'] << 20) - (calib['H5'] * h)) + 16384) >> 15) *
         (((((((h * calib['H6']) >> 10) * (((h * calib['H3']) >> 11) + 32768)) >> 10) + 2097152) *
           calib['H2'] + 8192) >> 14))
    h = h - (((((h >> 15) * (h >> 15)) >> 7) * calib['H1']) >> 4)
    h = max(min(h, 419430400), 0)
    humidity = (h >> 12) / 1024.0

    return temperature, humidity, pressure

# --------- Main Program ---------
try:
    print("Initializing sensors...")
    aht10_init()
    bme280_init()
    bme280_calib = bme280_read_calibration()
    print("Sensors initialized. Reading data...")

    while True:
        temp_aht, hum_aht = aht10_read()
        temp_bme, hum_bme, press_bme = bme280_read(bme280_calib)

        print("--- Sensor Readings ---")
        print(f"AHT10 - Temp: {temp_aht:.2f} °C, Humidity: {hum_aht:.2f}%")
        print(f"BME280 - Temp: {temp_bme:.2f} °C, Humidity: {hum_bme:.2f}%, Pressure: {press_bme:.2f} hPa")
        print("------------------------\n")
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopping...")
    bus.close()
