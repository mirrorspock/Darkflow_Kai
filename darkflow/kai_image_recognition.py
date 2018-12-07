import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


# %config InlineBackend.figure_format = 'svg'

options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'thresh': 0.3,
    'gpu': 0
}

tfnet = TFNet(options)

img = imread('test.jpeg', cv2.IMREAD_COLOR)


result = tfnet.return_predict(img)

print(result)

tl = (result[0]['topleft']['x'],result[0]['topleft']['y'])
br = (result[0]['bottomright']['x'],result[0]['bottomright']['y'])
label = result[0]['label']

img = cv2.rectangle(img, tl, br, (0,255,0), 2)
img = cv2.putText(img, label, tl ,cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0),2 )

plt.imshow(img)
plt.show()
