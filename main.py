from cv2 import *
cam = 0
camcap =VideoCapture(cam)
result, image = cam.read()

if result:
    imshow("window",image)
    imwrite("window.png",image)

    waitKey(0)
    destroyWindow("window")
else:
    print("nothing found")

