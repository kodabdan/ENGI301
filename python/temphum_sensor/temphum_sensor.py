import time
import busio
import board
import digitalio

import adafruit_ahtx0

# Initialize the I2C1 ports of the PocketBeagle

i2c = board.I2C()

aht10 = adafruit_ahtx0.AHTx0(i2c)

def __init__(self)
    

def aht10_read():
    """
    Queries AHT10 sensor
    Outputs temperature (in celsius) and humidity (%) readings
    """
    return aht10.temperature, aht10.relative_humidity
    
    
if __name__ == '__main__':
        temp_rd = aht10_read()[0]
        humi_rd = aht10_read()[1]
        print("Temperature: ")
        print(temp_rd)
        print("Humidity: ")
        print(humi_rd)
        