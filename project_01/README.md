This software is designed to run a plant care device using a 16x2 LCD display, a moisture sensor, a temperature and humidity sensor, 
a potentiometer, and a buzzer connected to a Pocketbeagle. The software is writen in the Python3 environment.

The code includes drivers for each of these hardware devices as well as a file to configure the pins for the project, a main driver,
and a run file. The project is run in cloud9 and is not set to automatically boot up using the code provided in this repository, that
will have to be adjusted by the user. All of the files in this repository must be downloaded for this program to work.

The instructions for the hardware for this device can be found on the following hackster page:
https://www.hackster.io/511865/plant-health-monitor-and-reminder-5650f4

After setup of the hardware, each of the LCD, moisture sensor, potentiomter, buzzer, and temp/humidity sensor classes have a test so
that you can check the connections between your devices. Keep in mind the pins used in the different class instances.

The projects will require installation of python to the cloud9 environment, and the commands to do that are listed below:

  sudo apt-get update3

  sudo apt-get update3. sudo apt-get install build-essential python-dev python-setuptools python-smbus -y

The temperature and humidity sensor requires the following command:

  sudo pip3 install --upgrade Adafruit_BBIO

The LCD display is an i2c device, so in the linux terminal the permissions can be adjusted using the command
  sudo chmod 666 i2c*

The sensors and potentiometer pass data to the main driver, which communicates with the LCD display as well as the buzzer for the outputs.
The potentiometer can be rotated to change voltage level, which controls the LCD. The sensors are not interacted with and collect data.

The program can be made by adding the following line to the cronlog:
@reboot sleep 30 && bash /var/lib/cloud9/ENGI301/python/plant_care_device/run > /var/lib/cloud9/logs/cronlog 2>&1

Have fun taking care of your plant!



