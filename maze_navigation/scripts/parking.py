#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

def park_robot():
    rospy.init_node('park_robot', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    twist = Twist()
    twist.linear.x = 0.2  # Move forward to park
    pub.publish(twist)
    time.sleep(2)  # Adjust this time based on testing

    twist.linear.x = 0.0  # Stop
    pub.publish(twist)
    print("Robot parked.")

if __name__ == "__main__":
    park_robot()

