#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Pose

from std_msgs.msg import String

bottle = False
(x0,y0) = (-1,-1)
depth = -1
one_bottle = Pose()

pub = rospy.Publisher('/bottle', Pose, queue_size=1)

def callback():
    global bottle
    if bottle == True :
        pub.publish(one_bottle)

class LoadFeature(object):

    def __init__(self):
    
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.image_depth_sub = rospy.Subscriber("/camera/depth/image_raw",Image,self.camera_depth_callback)
        self.pose_sub = rospy.Subscriber("/odom",Pose,self.position_callback)
        self.bridge_object = CvBridge()
        self.x = 4

    def camera_callback(self,data):

        global bottle
        global x0
        global y0

        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        #Once we read the image we need to change the color space to HSV
        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        #Hsv limits are defined
        #here is where you define the range of the color you are looking for
        #each value of the vector corresponds to the H,S & V values respectively

        min_red = np.array([0,25,40])
        max_red = np.array([0,255,255])

        #This is the actual color detection 
        #Here we will create a mask that contains only the colors defined in your limits
        #This mask has only one dimention, so its black and white }
        mask_r = cv2.inRange(hsv, min_red, max_red)

        kernel = np.ones((7,7),np.uint8)
        dilation = cv2.dilate(mask_r,kernel,iterations = 3)
        cv2.imwrite('/home/user/catkin_ws/src/students_package/challenge_2/image/mask_gris.png',dilation)
        #We use the mask with the original image to get the colored post-processed image
        res_r = cv2.bitwise_and(cv_image,cv_image, mask= dilation)

        cv2.imshow('Detection',res_r)

        cv2.waitKey(1)

        def position(M) :
            for y in range (len(M[0])):
                for x in range(len(M)):
                    if 25<M[x][y][1]<255 and 40<M[x][y][2]<255 :
                        bottle = True
                        return (x,y)
            return (-1,-1)

        (x0,y0) = position(res_r)
    
    def camera_depth_callback(self, data):

        global bottle
        global depth

        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="32FC1")
        except CvBridgeError as e:
            print(e)
        
        if bottle & (not (x0,y0)==(-1,-1)):
            depth = cv_image[x0][y0]

    def position_callback(self, data):

        global bottle
        global depth
        global one_bottle

        if bottle & depth>0 :
            one_bottle.x = data.position.x + depth*data.orientation.z
            one_bottle.y = data.position.y + depth*data.orientation.w




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