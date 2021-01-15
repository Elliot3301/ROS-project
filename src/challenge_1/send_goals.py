#! /usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionFeedback, MoveBaseActionGoal, MoveBaseActionResult, MoveBaseFeedback, MoveBaseGoal, MoveBaseResult
from geometry_msgs.msg import Pose, PoseStamped

def feedback_callback(feedback):
    global goal
    
rospy.init_node('send_goal_action_client')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose = PoseStamped()
goal.target_pose.header.frame_id = 'map'

pose1 = Pose()
pose1.position.x = rospy.get_param('/send_goals/point1/position/x')
pose1.position.y = rospy.get_param('/send_goals/point1/position/y')
pose1.orientation.z = rospy.get_param('/send_goals/point1/orientation/z')
pose1.orientation.w = rospy.get_param('/send_goals/point1/orientation/w')

pose2 = Pose()
pose2.position.x = rospy.get_param('/send_goals/point2/position/x')
pose2.position.y = rospy.get_param('/send_goals/point2/position/y')
pose2.orientation.z = rospy.get_param('/send_goals/point2/orientation/z')
pose2.orientation.w = rospy.get_param('/send_goals/point2/orientation/w')

while not rospy.is_shutdown():
    goal.target_pose.pose = pose1
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()

    goal.target_pose.pose = pose2
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()