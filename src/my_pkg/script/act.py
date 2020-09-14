#! /usr/bin/env python
import rospy

from geometry_msgs.msg import Twist

class tur :
    def __init__(self):
        rospy.init_node('move')
        self.__pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=1)
        self.__msg = Twist()
    def set_vel(self,v,w):
        self.__msg.linear.x=v
        self.__msg.angular.z=w

        self.__pub.publish(self.__msg)
