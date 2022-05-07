# EmbeddedMachineLearning-RaspberryPi

Project to deploy a Machine Learning Model on a Rasberry Pi

## Notes

- RasberryPi Credentials:
  - User: pi
  - Passwd: raspberry
- Wifi Connection:
  - PC yeshey-hotspot: 
  - Mobile Hotspot: ssh pi@192.168.208.219
  - static IP, connected to Yeshey-TP-LINK: ssh pi@192.168.0.103
  - Commands:
    - `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf` - file that says wich networks it will connect to
    - `sudo iwlist wlan0 scanning | grep ESSID` - show available wlan connections
    - `iwconfig | grep wlan0` - show currently active wlan connection

## Logical flow of.. steps

- Get DataSet of faces (like from https://thispersondoesnotexist.com)
- Label your dataset with something like https://github.com/tzutalin/labelImg
- Train Model in your home PC GPU 
  - check the links and info in MS Teams to do that
- Convert the model to *tensorflow lite model*, to run on your Coral TPU
  - Or search for how to make it run on Coral TPU Stick
- Load it to rasberry Pi and make it work somehow.
  - it has camera, Coral TPU, Keyboard.