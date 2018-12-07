import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'thresh': 0.3,
    'gpu': 0
}

tfnet = TFNet(options)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]
capture = cv2.VideoCapture('videofile_1080_2fps.avi')

# for color in colors:
# 	print(color)

while (capture.isOpened()):
	stime = time.time()
	ret, frame = capture.read()
	results = tfnet.return_predict(frame)
	if ret:
		for color, result in zip(colors, results):
			tl = (result['topleft']['x'],result['topleft']['y'])
			br = (result['bottomright']['x'],result['bottomright']['y'])
			label = result['label']
			frame = cv2.rectangle(frame, tl, br, (0,255,0), 2)
			frame = cv2.putText(frame, label, tl ,cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2 )
		cv2.imshow('frame', frame)
		print('FPS {:.1f}'.format(1 / (time.time() - stime)))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		capture.realease()
		cv2.destroyAllWindows()
		break


