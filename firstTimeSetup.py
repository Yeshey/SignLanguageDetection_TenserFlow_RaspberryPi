import wget 
import zipfile
import os
import tarfile

print("Running first time setup...")

# check folders
ckckfldrs = os.listdir("./TensorFlow/workspace/training_demo/")

if all( i != "images" for i in ckckfldrs):
    os.mkdir("./TensorFlow/workspace/training_demo/images")
    # Downloading database
    print("thanks to https://public.roboflow.com/object-detection/american-sign-language-letters/1 for dataset")
    print("Downloading Dataset to ./TensorFlow/workspace/training_demo/images/...")
    url = 'https://public.roboflow.com/ds/wdx82NVcss?key=lyVASY8xq4'
    path = './TensorFlow/workspace/training_demo/images/'
    wget.download(url,out = path)

    print("\nUnzipping...")
    zipPath = os.listdir("./TensorFlow/workspace/training_demo/images/")
    zipPath = "./TensorFlow/workspace/training_demo/images/" + str(zipPath[0])
    print(zipPath)
    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
        zip_ref.extractall("./TensorFlow/workspace/training_demo/images/")

    for item in os.listdir("./TensorFlow/workspace/training_demo/images/"): # loop through items in dir
        if item.endswith(".zip"): # check for ".zip" extension
            os.remove("./TensorFlow/workspace/training_demo/images/"+ item)
else:
    print("images folder already exists")

if all( i != "pre-trained-models" for i in ckckfldrs):
    os.mkdir("./TensorFlow/workspace/training_demo/pre-trained-models")
    # Downloading Pre-trained model
    print("using SSD ResNet50 V1 FPN 640x640 pre-trained model from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md")
    print("Downloading pre-trained model to ./TensorFlow/workspace/training_demo/pre-trained-models/..")
    url = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz'
    path = './TensorFlow/workspace/training_demo/pre-trained-models/'
    wget.download(url,out = path)

    print("\nUnzipping...")
    zipPath = os.listdir("./TensorFlow/workspace/training_demo/pre-trained-models/")
    zipPath = "./TensorFlow/workspace/training_demo/pre-trained-models/" + str(zipPath[0])
    tar = tarfile.open(zipPath, "r:gz")
    tar.extractall('./TensorFlow/workspace/training_demo/pre-trained-models/')
    tar.close()

    for item in os.listdir("./TensorFlow/workspace/training_demo/pre-trained-models/"): # loop through items in dir
        if item.endswith(".tar.gz"): # check for ".zip" extension
            os.remove("./TensorFlow/workspace/training_demo/pre-trained-models/"+ item)
else:
    print("pre-trained-models folder already exists")
