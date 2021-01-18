#! /usr/bin/env python



import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

rospy.init_node('test_1')
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

def callback(msg):
    global move
    if msg.ranges[360] < 1:   
        move.linear.x = 0.0
        move.angular.z = 1.0
    
    if msg.ranges[350] < 1:   
        move.linear.x = 0.0
        move.angular.z = 1.0

    if msg.ranges[370] < 1:   
        move.linear.x = 0.0
        move.angular.z = -1.0

    if msg.ranges[360] >= 1:
        move.linear.x = 0.5
        move.angular.z = 0.0

    pub.publish(move)


sub = rospy.Subscriber('kobuki/laser/scan', LaserScan, callback)
rospy.spin()