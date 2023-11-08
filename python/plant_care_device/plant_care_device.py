"""
--------------------------------------------------------------------------
Plant_Care_Device
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

Display temperature, humidity, and moisture data from a plant on an LCD display

"""
import time
import busio
import board
import digitalio

import adafruit_ahtx0
import potentiometer
import hd44780 as LCD
import moisture_sensor


# Initialize the I2C1 ports of the PocketBeagle

i2c = board.I2C()

aht10 = adafruit_ahtx0.AHTx0(i2c)



# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

potentiometerpin = "P1_19"
moisturepin = "P2_28"
rs = "P1_2"
enable = "P1_4"
d4 = "P2_2"
d5 = "P2_4"
d6 = "P2_6"
d7 = "P2_8"

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Plant_Care_Device():
    """ Plant Care Device """
    potentiometer     = None
    moisture_sensor   = None
    temphum_sensor    = None
    LCD               = None
    
    
    def __init__(self, potentiometerpin, moisturepin, i2c_bus=1, i2c_address=0x38):
        """ Initialize variables and set up display """
        
        self.potentiometer     = potentiometer.Potentiometer(potentiometerpin)
        self.moisture_sensor   = moisture_sensor.Moisture_Sensor(moisturepin)
        self.temphum_sensor    = aht10
        self.LCD               = LCD.LCD(rs,enable,d4,d5,d6,d7,16,2)
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
        # Initialize Display
        self.LCD.clear()
        
    # End def


    def run(self):
        """Execute the main program."""
        datamessages = ["Moisture Level: \n" , "Temperature: \n" , "Humidity: \n"]
        
        self.LCD.message("Good Morning\nBrendan")
        time.sleep(4)
        self.LCD.message(moisturemessage + str(round(self.moisture_sensor.get_percentage()),1))
        
        while(1):
            onpotentiometerval = self.potentiometer.get_voltage()
            difference = 0
            while(difference < 0.3):
                difference = self.potentiometer.get_voltage()-basepotentiomerval
            if (difference <0):
                
                
            
            
            moisture = str(round(self.moisture_sensor.get_percentage(),1))
            percentagedisp = '\n'+ moisture + '%'
            self.LCD.message()
            self.LCD.message(percentagedisp)
            time.sleep(4)
            self.LCD.clear()
            """
            basepotentiometerval = self.potentiometer.get_voltage()
            if (self.potentiometer.get_voltage()-basepotentiometerval > 0.3):
                self.LCD.clear()
                
                
            curpotentiometerval = self.potentiometer.get_voltage()
            print(round(potentiometerval,3))
            
            if potentiometerval < 0.6:
                moisture = str(self.moisture_sensor.get_value())
                percentagedisp = '\n'+ moisture + '%'
                self.LCD.message("Moisture Level: ")
                self.LCD.message(percentagedisp)
                
            elif potentiometerval < 1.2:
                temp = str(round(aht10.temperature,2))
                tempdisp = '\n'+ temp
                self.LCD.message("Temperature: ")
                self.LCD.message(tempdisp)
            else:
                hum = str(round(aht10.relative_humidity,2))
                humdisp = '\n' + hum
                self.LCD.message("Humidity: ")
                self.LCD.message(humdisp)
            """

    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
        self.LCD.clear()
        
        # Button does not need any cleanup code
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the people counter
    plantcare = Plant_Care_Device("P1_19", "P1_21")

    try:
        # Run the people counter
        plantcare.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        plantcare.cleanup()

    print("Program Complete")

