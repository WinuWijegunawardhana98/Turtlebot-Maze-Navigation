#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MazeNavigator:
    def __init__(self):
        rospy.init_node('maze_navigator', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.laser_subscriber = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.vel_msg = Twist()
        self.regions = {
            'front': 0,
            'left': 0,
            'right': 0
        }
        rospy.loginfo("Maze Navigator Node Initialized")  # Add logging
        self.rate = rospy.Rate(10)

    def laser_callback(self, data):
        self.regions = {
            'front': min(min(data.ranges[0:10] + data.ranges[-10:]), 3.0),
            'left': min(min(data.ranges[80:100]), 3.0),
            'right': min(min(data.ranges[-100:-80]), 3.0)
        }
        rospy.loginfo("Regions: {self.regions}")  # Add logging

    def navigate(self):
        rospy.loginfo("Starting Navigation")  # Add logging
        while not rospy.is_shutdown():
            if self.regions['front'] > 1.0:
                self.vel_msg.linear.x = 0.2
                self.vel_msg.angular.z = 0.0
            elif self.regions['front'] < 1.0:
                self.vel_msg.linear.x = 0.0
                self.vel_msg.angular.z = 0.5
            elif self.regions['left'] < 0.5:
                self.vel_msg.linear.x = 0.2
                self.vel_msg.angular.z = -0.3
            elif self.regions['right'] < 0.5:
                self.vel_msg.linear.x = 0.2
                self.vel_msg.angular.z = 0.3

            self.velocity_publisher.publish(self.vel_msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        navigator = MazeNavigator()
        navigator.navigate()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node Terminated")

