#! /usr/bin/env python
import rospy

from act import tur 
t1= tur()

w = 1 
r = 1 
v = w *r 

while not rospy.is_shutdown():

    t1.set_vel(v,w)
