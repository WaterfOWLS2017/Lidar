#!/usr/bin/env python
import serial
import rospy
from sensor_msgs import LaserScan
from lidar.srv import ScanRange # import custom ros service type


SERIAL_BAUD_RATE = 115200
SERIAL_COMM_PORT = ''
ROS_NODE_NAME = 'lidar_node'
ROS_SERVICE_TOPIC = '/lidar_control'

def main():
    rospy.init_node(ROS_NODE_NAME) # create a new ros node
    lidar_pub = rospy.Publisher('lidar_scans', LaserScan, queue_size=10)
    lidar_control_service = rospy.Service(ROS_SERVICE_TOPIC)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():

# end def main()

if __name__ == '__main__':
    main()
# eof
