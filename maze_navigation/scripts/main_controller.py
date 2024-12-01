#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time

class TurtleBot3Controller:
    def __init__(self):
        rospy.init_node('turtlebot3_controller', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = Twist()

        # Subscribe to LIDAR scan data for maze navigation
        rospy.Subscriber('/scan', LaserScan, self.lidar_callback)

        # Control variables
        self.wall_distance = 0.5  # Threshold for walls
        self.maze_completed = False  # Track if maze is solved

    # Callback function to control robot movement in the maze
    def lidar_callback(self, data):
        if self.maze_completed:
            return  # Stop processing if the maze is completed

        front = min(min(data.ranges[0:30]), min(data.ranges[330:359]))  # Front
        left = min(data.ranges[60:120])  # Left side
        right = min(data.ranges[240:300])  # Right side

        if front < self.wall_distance:
            self.twist.angular.z = -0.5  # Turn right
            self.twist.linear.x = 0.0
        elif left < self.wall_distance:
            self.twist.linear.x = 0.2  # Move forward with slight left turn
            self.twist.angular.z = 0.1
        else:
            self.twist.linear.x = 0.3  # Move forward
            self.twist.angular.z = 0.0

        self.pub.publish(self.twist)  # Send movement commands

    # Function to navigate through the maze
    def navigate_maze(self):
        print("Navigating the maze...")
        rospy.sleep(10)  # Simulate 10 seconds of maze navigation

        # Stop the robot after solving the maze
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

        self.maze_completed = True  # Mark maze as completed
        print("Maze completed.")

    # Mock slit detection function
    def detect_slits(self):
        open_slits = 2  # Mock detection of 2 open slits
        print("Detected {open_slits} open slits.")
        return open_slits

    # Function to select path based on slit detection
    def select_path(self, open_slits):
        if open_slits == 1:
            print("Following Path 1...")
        elif open_slits == 2:
            print("Following Path 2...")
        elif open_slits == 3:
            print("Following Path 3...")
        else:
            print("Error: Invalid number of open slits.")

    # Function to park the robot
    def park_robot(self):
        print("Parking the robot...")
        self.twist.linear.x = 0.2  # Move forward into parking zone
        self.pub.publish(self.twist)
        time.sleep(2)  # Adjust time as needed

        # Stop the robot
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)
        print("Robot parked successfully.")

    # Main function to run the entire task flow
    def run(self):
        print("Starting TurtleBot3 tasks...")
        self.navigate_maze()  # Step 1: Navigate maze
        open_slits = self.detect_slits()  # Step 2: Detect slits
        self.select_path(open_slits)  # Step 3: Select path
        self.park_robot()  # Step 4: Park the robot
        print("All tasks completed successfully!")

if __name__ == "__main__":
    try:
        controller = TurtleBot3Controller()
        controller.run()
    except rospy.ROSInterruptException:
        print("ROS node interrupted.")

