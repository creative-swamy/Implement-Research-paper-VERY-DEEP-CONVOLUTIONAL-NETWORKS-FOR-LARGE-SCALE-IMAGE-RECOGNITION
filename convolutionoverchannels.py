# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:01:02 2019
Convolutions over channels
"""

from keras.models import Sequential
from keras.layers import Conv2D

model =Sequential()
#Same padding means: size of the input and output should be same. In this case 256*256
model.add(Conv2D(512, (3, 3), padding='same', activation='relu', input_shape=(256, 256, 3)))
#Scalling up number of features
model.add(Conv2D(1024, (1, 1), activation='relu'))

model.summary()