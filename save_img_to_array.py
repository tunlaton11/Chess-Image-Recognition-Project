import cv2
import os
import numpy as np

img_array = []
label_array = []

directory = 'Chess_formatted'

for _classname in sorted(os.listdir(directory)):
    for _name in sorted(os.listdir(directory + '/' + _classname)):
        path = directory + '/' + str(_classname) + '/' + str(_name)

        # Convert color and resize color
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (112, 112), interpolation=cv2.INTER_AREA)

        img_array.append(np.array(img))
        label_array.append(_classname)

img_array = np.array(img_array)
label_array = np.array(label_array)

np.save('img_array', img_array)
np.save('label_array', label_array)
