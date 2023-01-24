import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

x=0
y=0
z=0
yaw=0

def pose_callback(pose_message):
    global x
    global y, z, yaw
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta


def move(speed, distance):
    velocity_message = Twist()
    x0=x
    y0=y
    velocity_message.linear.x = speed
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)    
    cmd_vel_topic='/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    while True :
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        
        distance_moved = distance_moved+abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
        if  not (distance_moved<distance):
            break
    
    velocity_message.linear.x =0
    velocity_publisher.publish(velocity_message)

def rotate(angular_speed, angle):
    velocity_message = Twist()
    angular_speed_rad = math.radians(abs(angular_speed))

    velocity_message.angular.z = abs(angular_speed_rad)

    loop_rate = rospy.Rate(10)

    cmd_vel_topic='/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True:
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        angle_moved = (t1-t0)*angular_speed
        print(angle_moved)
        loop_rate.sleep()

        if (angle_moved >= angle):
            break
    
    velocity_message.angular.z = 0.0
    velocity_publisher.publish(velocity_message)
        

if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, pose_callback)

        time.sleep(2)
        rotate(100,60)
        time.sleep(2)
        move (2.0, 7.0)
        time.sleep(2)
        rotate(100, 120)
        time.sleep(2)
        move (2.0, 7.0)
        rotate(100, 120)
        time.sleep(2)
        move (2.0, 7.0)
        time.sleep(2)
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
