"""
--------------------------------------------------------------------------
Moisture Sensor Driver
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

Moisture Sensor Driver

  This driver is built for a 3 pin moisture sensor connected to a gpio pin

Software API:

  moisture_sensor(pin)
    - Provide pin that the moisture sensor is connected to
    
    get_value()
    - provide the moisture value

"""
import Adafruit_BBIO.ADC as ADC

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Moisture_Sensor():
    """ moisture sensor class """
    pin              = None
    moisture_value   = None
    
    def __init__(self, pin):
        """ Initialize variables and set up the moisture sensor """
        if (pin == None):
            raise ValueError("Pin not provided for moisture sensor")
        else:
            self.pin = pin

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize LED

        ADC.setup()

    # End def


    def get_value(self):
        """ Get the value of the moisture sensor
        
           Returns:  Integer in [0, 4095]
        """
        # Read raw value from ADC

        return ADC.read_raw(self.pin)

    # End def
    
    def get_percentage(self):
        """
        Returns the soil moisture percentage
        """
        
        return 100 - (((self.get_value() - 1360) / 2700) * 100)
        
    # end def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    import time

    print("Moisture Sensor Test")

    # Create instantiation of the LED
    moisture_sensor = moisture_sensor("P1_19")
    
    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    print("Use Ctrl-C to Exit")
    
    try:
        while(1):
            # Print moisture value
            print("Moisture Level is: ")
            print(moisture_sensor.get_value())
            time.sleep(1)
            
            
    except KeyboardInterrupt:
        pass

    print("Test Complete")

