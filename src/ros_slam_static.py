import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def move_to_goal(goal_x,goal_7):

   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   goal.target_pose.pose.position =  Point(goal_x,goal_y,0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("Destination reached")
           return True

   else:
           rospy.loginfo("Navigation Failed")
           return False

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   x_goal = 1
   y_goal = 2
   move_to_goal(x_goal,y_goal)
   rospy.spin()
