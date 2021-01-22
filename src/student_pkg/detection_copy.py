#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import matplotlib.pyplot as plt

from std_msgs.msg import String

bottle = False

pub = rospy.Publisher('/bottle', String)

def callback():
    global bottle
    if bottle == True :
        pub.publish("bottle")

class LoadFeature(object):

    def __init__(self):
    
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.bridge_object = CvBridge()
        self.x = 4

    def camera_callback(self,data):
        global bottle
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        img = cv_image
  

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h,s,v= cv2.split(hsv)
        ret_h, th = cv2.threshold(h,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


        im_floodfill = th.copy()
        h, w = th.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(im_floodfill, mask, (0,0), 255)
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)
        th = th | im_floodfill_inv


        _, contours, _ = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(img, contours, -1, (255,255,255), -1)
        for i in range (0, len(contours)) :
            #mask_BB_i = np.zeros((len(th),len(th[0])), np.uint8)
            x,y,w,h = cv2.boundingRect(contours[i])
            if 1<w<8 and 1<h<8 :
                print(w,h)
                cv2.drawContours(img, contours, i, (255,255,255), -1)
                pts = np.array([[x, y], [x-w, y], [x-w, y-h], [x, y-h], [200, 70], [110, 20]], np.int32)
                pts = pts.reshape((-1, 1, 2))
                result = cv2.polylines(img, pts, True, (50,0,255), 3, cv2.LINE_AA)
                #BB_i=cv2.bitwise_and(img,img,mask=mask_BB_i)
            
        cv2.imshow('Detection',img)       

        cv2.waitKey(1)


def main():
    global bottle
    load_feature_object = LoadFeature()
    rospy.init_node('detection', anonymous=True)
    
    try:
        callback()
        rospy.spin()
        
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()