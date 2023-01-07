
## System Setup

Setup the ROS(noetic) workspace in Ubuntu 20.04 (Focal)
We are using PX4 Autopilot library function. To set up run the following code.

```bash
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```
To test whether all the configuration are working. Run the following test script,
Raspberrypi should be able to connnect to the PX4 and the motor should start spinning.

```bash
cd Onboard-pi
python3 test_connect.py # Change the 'connction_string' in code to the connected USB port
# setup the correct Baud rate for UART communication
```




## Streaming Video over WiFi

Since the OnBoard Computer Raspberrypi run the Raspbian Lite version, we will be 
using socket programming to get the video feed over WiFi

Run the following script on Laptop (Ground  Station)

```bash
cd Groundstation
python3 laptop_server_img.py # Modify the ip address of the HOST computer
```
Run the following script on Raspberrypi

```bash
cd OnBoard-pi
python3 pi_client.py # Put the Raspberrypi ip address and set the port numbetr same as host
```


    
## Camera Callibration
Every Camera is slightly different even if they are of the same model. So they must be callibrated before usage.
```python3
cd Onboard-pi
python3 Capture_image.py
```
Capture Images of Checkboard in different orientation by pressing 'Space'. Store the images captured in the directory check_images

```python3
python3 camera_calibration.py
```
This will calibrate the camera by processing the images of the checkboard in the check_images folder and genarating the following matrix

calibration_matrix1.npy 

distortion_coefficients1.npy

This matrix is used in the script of AruCO detection

## Hardware parameter tuning for NO_GPS mode Using QGroundControl
```param
ARMING_GPS_USE DISABLED
AHRS_GPS_USE DISABLED
EK3_SRC1_POSXY None
EK3_SRC1_VELXY None
EK3_SRC1_VELZ None
COMPASS_USE DISABLED
COMPASS_USE2 DISABLED
COMPASS_USE3 DISABLED
```
## Detecting Pose from AruCO marker
Run the following script to detect the pose of the drone using AruCO marker

```python3
cd Onboard-pi
python3 script.py
```
