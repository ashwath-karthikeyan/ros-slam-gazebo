from time import sleep
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from time import sleep

global pose_val

#import the pose value
def callback_message(message):
    x = message.x
    y = message.y
    theta = message.theta
    pose_val = [x,y,theta]
    print ("x: ",x,"\ny: ",y,"\ntheta: ",theta,"\n")

def pose_update():

    rospy.init_node('pose_sub', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose, callback_message)


    rospy.spin()

    sleep(1)

def move():
    linear_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    rospy.init_node('linear_speed', anonymous=True)

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1



if __name__ == '__main__':
    pose_update()

