import cv2
import time
import getpass
import os

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

img_counter = 0
#getUser = getpass.getuser()
save = "/home/mahima/images"
for i in range(50):
  ret, frame = cam.read()
  cv2.imshow("test", frame)
  time.sleep(5)
  img_name = "frame_{}.jpg".format(img_counter)
  cv2.imwrite(os.path.join(save, img_name), frame)
  print("{} written!".format(img_name))
  img_counter += 1

cam.release()

