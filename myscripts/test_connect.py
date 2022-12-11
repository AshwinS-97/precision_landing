from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

#-- Connect to the vehicle
import argparse
parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()

connection_string = "/dev/ttyUSB0"


print("Connection to the vehicle on %s"%connection_string)
vehicle = connect(connection_string,baud=57600, wait_ready=True)

#-- Define the function for takeoff
def arm_and_takeoff(tgt_altitude):
    print("Arming motors")
           
    vehicle.mode = VehicleMode("GUIDED_NOGPS")
    vehicle.armed = True
    
    while not vehicle.armed: time.sleep(1)
    print("Yes Armed")
    print("Takeoff")
    vehicle.simple_takeoff(tgt_altitude)
    
           
        
#------ MAIN PROGRAM ----
arm_and_takeoff(10)
##arm_and_takeoff_nogps(2.5)
#set_attitude(thrust = 0.1)
time.sleep(2)
#set_attitude(thrust = 0)

#-- set the default speed

