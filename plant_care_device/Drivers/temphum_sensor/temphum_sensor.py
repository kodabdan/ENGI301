"""
--------------------------------------------------------------------------
Temperature & Humidity Sensor Driver
--------------------------------------------------------------------------
License:   
Copyright 2023 - Brendan Hlibok

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Temperature and Humidity Sensor Driver for PocketBeagle

Software API:

 aht10_read() returns the temperature and humidity reading from the sensor

"""

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
        
