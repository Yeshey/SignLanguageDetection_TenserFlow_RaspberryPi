# EmbeddedMachineLearning-RaspberryPi

Project to deploy a Machine Learning Model on a Rasberry Pi

## Setup

- follow the `SignLanguageDetection.ipynb` file to setup, train and run the model

## Notes

- [American sign language letters image](https://www.researchgate.net/publication/346023992/figure/fig1/AS:959642733649922@1605808065864/Fingerspelling-in-American-Sign-Language-which-represents-26-letters-and-10-digits-with.jpg)
- See Nvidia available memory in linux with `watch -n 0.1 nvidia-smi`
- Activate environment `conda activate signLanguageDetector'
- RasberryPi Credentials:
  - User: pi
  - Passwd: raspberry
- Wifi Connection:
  - Connect using the hostname: `ssh pi@raspberrypi`
  - Connecting using ip (connected to yeshey-hotspot): 'ssh pi@192.168.12.230'
  - Commands:
    - `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf` - file that says wich networks it will connect to
    - `sudo iwlist wlan0 scanning | grep ESSID` - show available wlan connections
    - `iwconfig | grep wlan0` - show currently active wlan connection

## Logical flow of.. steps

- [Check Teams](https://teams.microsoft.com/_#/school/conversations/General?threadId=19:r1IGvssAqzPBmvBm8wHKg16bVGiFaaG_P8K87bbHE941@thread.tacv2&ctx=channel)
  - >  For Everyone doing an object detection: I recommend using [this API for Training](https://github.com/tensorflow/models/tree/master/research/object_detection) A very good tutorial from start to finish can be found here: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html General This also works in the ICC 
  - > General for everyone wanting to annotate images, I can recommend https://supervise.ly/
  - > General Tutorial for image classification: https://www.tensorflow.org/hub/tutorials/tf2_image_retraining
- Get DataSet of faces (like from https://thispersondoesnotexist.com)
  - Or find datasets in this site for example: [paperswithcode.com](https://paperswithcode.com) 
- Label your dataset with something like https://github.com/tzutalin/labelImg
- Train Model in your home PC GPU 
  - check the links and info in MS Teams to do that
- Convert the model to *tensorflow lite model*, to run on your Coral TPU
  - Or search for how to make it run on Coral TPU Stick
- Load it to rasberry Pi and make it work somehow.
  - it has camera, Coral TPU, Keyboard.

## references
- [Tenserflow guide](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)
- [American Sign Language Letters Dataset](https://public.roboflow.com/object-detection/american-sign-language-letters/1)
- [had to do this before training](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md#python-package-installation)