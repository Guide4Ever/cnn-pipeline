import os
import cv2

import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras

from alibi_detect.od import OutlierAE, OutlierVAE
from alibi_detect.utils.visualize import plot_instance_score, plot_feature_outlier_image

SIZE = 256

dataset = []
zdravedir = "zdraveMod"
good_images = os.listdir(zdravedir)

for i, image_name in enumerate(good_images):
  if (image_name.split('.')[1] == 'png'):
    image = cv2.imread(zdravedir + '/' + image_name, cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image, (SIZE, SIZE))
    image = np.array(image)
    image = image.reshape(image.shape[0], image.shape[1], 1)
    dataset.append(image)

dataset = np.array(dataset)
print(f"There are {len(dataset)} images")
print(f"dataset.shape: {dataset.shape}")

train_percentage = 50
train = dataset[0:int(len(dataset)*train_percentage/100)]
test = dataset[int(len(dataset)*train_percentage/100):len(dataset)]
print(f"Train length: {len(train)}, test length: {len(test)}")


train = train.astype('float32') / 65535.
test = test.astype('float32') / 65535.