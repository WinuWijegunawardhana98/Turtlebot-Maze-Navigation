# Turtlebot-Maze-Navigation
This ROS Kinetic project programs TurtleBot3 to autonomously navigate mazes using LIDAR, detect open slits with mock logic, select paths, and park in a designated zone. It combines Python-based control scripts for simulation (Gazebo) and hardware deployment, supporting modular and scalable tasks.


![Screenshot 2024-12-01 194605](https://github.com/user-attachments/assets/4a5a12d5-0136-4c5a-904e-1e8da7ee9790)


#Step 1
The robot has to navigate through the maze autonomously and find the exit point. You may use any
algorithm to do this task. The width of the inside paths of the maze would be 10 inches wider than
your robot. The maze may be slightly different at the final demonstration. Marks would be based on
the time of completion of the maze.
20 × 𝑡𝑚𝑖𝑛
𝑀𝑎𝑟𝑘𝑠 𝑓𝑜𝑟 𝑆𝑜𝑙𝑣𝑖𝑛𝑔 𝑡ℎ𝑒 𝑀𝑎𝑧𝑒 =𝑡
𝑡 = 𝑇𝑖𝑚𝑒 𝑡𝑎𝑘𝑒𝑛 𝑏𝑦 𝑦𝑜𝑢𝑟 𝑟𝑜𝑏𝑜𝑡 𝑡𝑜 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒 𝑡ℎ𝑒 𝑚𝑎𝑧𝑒
𝑡𝑚𝑖𝑛= 𝑀𝑖𝑛𝑖𝑚𝑢𝑚 𝑡𝑖𝑚𝑒 𝑡𝑎𝑘𝑒𝑛 𝑏𝑦 𝑎 𝑟𝑜𝑏𝑜𝑡 𝑡𝑜 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒 𝑡ℎ𝑒 𝑚𝑎𝑧𝑒

#Step 2
The robot may find a straight wall to its right, upon exiting the maze. The wall has three slits which
could be opened or closed randomly when performing your demonstration. The robot must identify
the number of open slits in the wall while navigating forward to reach the end of the wall.

#Step 3
There will be three non-overlapping paths at the end of the straight wall. The robot must choose the
correct path based on the number of open slits detected in the straight wall.
Example: 1 Open slit detected → Choose path 1
The paths are not marked or guided by any means. The robot must be pre-programmed with all the
three paths to follow the corresponding trajectory. Robot should be stopped within the marked
parking zone after completing the trajectory
