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
pose1.position.x = rospy.get_param('/bottles/bottle1/position/x')
pose1.position.y = rospy.get_param('/bottles/bottle1/position/y')
pose1.orientation.z = rospy.get_param('/bottles/bottle1/orientation/z')
pose1.orientation.w = rospy.get_param('/bottles/bottle1/orientation/w')

pose2 = Pose()
pose2.position.x = rospy.get_param('/bottles/bottle2/position/x')
pose2.position.y = rospy.get_param('/bottles/bottle2/position/y')
pose2.orientation.z = rospy.get_param('/bottles/bottle2/orientation/z')
pose2.orientation.w = rospy.get_param('/bottles/bottle2/orientation/w')

pose3 = Pose()
pose3.position.x = rospy.get_param('/bottles/bottle3/position/x')
pose3.position.y = rospy.get_param('/bottles/bottle3/position/y')
pose3.orientation.z = rospy.get_param('/bottles/bottle3/orientation/z')
pose3.orientation.w = rospy.get_param('/bottles/bottle3/orientation/w')

pose4 = Pose()
pose4.position.x = rospy.get_param('/bottles/bottle4/position/x')
pose4.position.y = rospy.get_param('/bottles/bottle4/position/y')
pose4.orientation.z = rospy.get_param('/bottles/bottle4/orientation/z')
pose4.orientation.w = rospy.get_param('/bottles/bottle4/orientation/w')

pose5 = Pose()
pose5.position.x = rospy.get_param('/bottles/bottle5/position/x')
pose5.position.y = rospy.get_param('/bottles/bottle5/position/y')
pose5.orientation.z = rospy.get_param('/bottles/bottle5/orientation/z')
pose5.orientation.w = rospy.get_param('/bottles/bottle5/orientation/w')

pose6 = Pose()
pose6.position.x = rospy.get_param('/bottles/bottle6/position/x')
pose6.position.y = rospy.get_param('/bottles/bottle6/position/y')
pose6.orientation.z = rospy.get_param('/bottles/bottle6/orientation/z')
pose6.orientation.w = rospy.get_param('/bottles/bottle6/orientation/w')

while not rospy.is_shutdown():
    goal.target_pose.pose = pose1
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()
    print("")
    print("Bottle 1")

    goal.target_pose.pose = pose2
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()
    print("")
    print("Bottle 2")

    goal.target_pose.pose = pose3
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()
    print("")
    print("Bottle 3")

    goal.target_pose.pose = pose4
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()
    print("")
    print("Bottle 4")

    goal.target_pose.pose = pose5
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()
    print("")
    print("Bottle 5")

    goal.target_pose.pose = pose6
    client.send_goal(goal, feedback_cb=feedback_callback)
    client.wait_for_result()
    print("")
    print("Bottle 6")