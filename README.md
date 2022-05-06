# EmbeddedMachineLearning-RaspberryPi

Project to deploy a Machine Learning Model on a Rasberry Pi

## Notes

- RasberryPi Credentials:
  - User: pi
  - Passwd: raspberry

## Logical flow of.. steps

- Get DataSet of faces (like from https://thispersondoesnotexist.com)
- Label your dataset with something like https://github.com/tzutalin/labelImg
- Train Model in your home PC GPU 
  - check the links and info in MS Teams to do that
- Convert the model to *tensorflow lite model*, to run on your Coral TPU
  - Or search for how to make it run on Coral TPU Stick
- Load it to rasberry Pi and make it work somehow.
  - it has camera, Coral TPU, Keyboard.