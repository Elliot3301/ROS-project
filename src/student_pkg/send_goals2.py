#! /usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionFeedback, MoveBaseActionGoal, MoveBaseActionResult, MoveBaseFeedback, MoveBaseGoal, MoveBaseResult
from geometry_msgs.msg import Pose, PoseStamped
from sensor_msgs.msg import LaserScan

def feedback_callback(feedback):
    global goal
    
rospy.init_node('send_goal_action_client')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose = PoseStamped()
goal.target_pose.header.frame_id = 'map'

pose1 = Pose()
pose1.position.x = input("x position : ")
pose1.position.y = input("y position : ")
pose1.orientation.z = input("z orientation : ")
pose1.orientation.w = input("w orientation : ")



def callback(msg):
    print(msg)
        
sub = rospy.Subscriber('/scan', LaserScan, callback)

goal.target_pose.pose = pose1
client.send_goal(goal, feedback_cb=feedback_callback)

while not rospy.is_shutdown() :
    msg = LaserScan()
    if msg.ranges[360] <= 2 :
        client.cancel_goal()
        rate = rospy.Rate(1500)
        goal.target_pose.pose = pose1
        client.send_goal(goal, feedback_cb=feedback_callback)
        rate.sleep()
    

