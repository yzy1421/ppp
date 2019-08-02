import cv2
import os
path='/home/zy3/Downloads/Scene-Classification-master/data/scene_classification_or/scene_classification_oringin'
os.chdir(path)
imgname='20180409_123025_2018-04-09_time0.jpg'
pic=cv2.imread(imgname)
pic=cv2.resize(pic,(400,400),cv2.INTER_CUBIC)
cv2.imshow('',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
