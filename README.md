# UCF-REU-SmartHome
IoT augmented physical scale model of a suburban home. An REU project performed at the University of Central Florida. Funded by the National Science Foundation.

## Usage
#### All code is written for python3

- data_collect_motors.py 
  * runs on the PiHat Raspberry Pi.
  * This code runs the motors based on what is described in sequences.py.  The current running sequence is demo().
- data_collect_sensors.py 
  * runs on the breadboard Raspberry Pi. 
  * This code does not to be touched outside of changing the frequency with which data is recorded.

Each pi collects its own data in the specified output file.  The data is then combined into one file by running combine_data_files.py.

## Debugging
- sequences.py 
  * contains the different purposeful motor movements to be run in conjunction with data collection of the motor states and the temperature and humidity in each of the rooms in the house.
- pin_control.py
  * contains the motor control methods as well as hard-coded values for the angles of the doors and windows to be closed flush.
  * also contains the dictionaries for the motors and their states
- debug_door_window.py
  * might be improperly spaced currently
  * present methods:
    * 'open all'
    * 'close all'
    * 'open all doors'
    * 'close all doors'
    * 'open all windows'
    * 'close all windows'
    * 'open ' + motor_pin_num
    * 'close ' + motor_pin_num
- code.py
  * present methods:
    * 'open ' + motor_name
    * 'close ' + motor_name
