#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
import thread
import threading
import time
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from std_msgs.msg import Float64  
import numpy
import rospy, sys 
import moveit_commander 
import math as m
from control_msgs.msg import GripperCommand 
import tf
from tf.transformations import *
import datetime
import urx

'''def callback1(pose): 
    global x1,y1,z1
    x1=pose.pose.position.x
    y1=pose.pose.position.y
    z1=pose.pose.position.z'''
  
def callback2(pose): 
    global x2,y2,z2
    x2=pose.pose.position.x
    y2=pose.pose.position.y
    z2=pose.pose.position.z

def callback3(pose): 
    global x3,y3,z3
    x3=pose.pose.position.x
    y3=pose.pose.position.y
    z3=pose.pose.position.z  


def listener(a,b): 
    pose=PoseStamped()     
    #rospy.Subscriber('vrpn_client_node/RigidBody01/pose',PoseStamped,callback1,queue_size = 1)   
    rospy.Subscriber('vrpn_client_node/RigidBody002/pose', PoseStamped, callback2,queue_size = 1)
    rospy.Subscriber('vrpn_client_node/RigidBody003/pose', PoseStamped, callback3,queue_size = 1)

    rospy.spin()


def MoveItIKDemo(): 
    a=datetime.datetime.now()
    thread.start_new_thread(listener,(0,0))
    
    global again
    while again:
        time.sleep(0.1)
        again = 0
    
    #a=datetime.datetime.now()
    #time.sleep(0.01)
    #第一关节角度
    '''b1=m.sqrt((z2-z3)**2+(x2-x3)**2)
    a1=m.sqrt((y2-y3)**2+b1**2)
    global jd1,jd3
    if y2>y3:
        jd1=-m.acos(b1/a1)
    else:
        jd1=m.acos(b1/a1)
#第二关节角度
    b2=m.sqrt((y1-y2)**2+(z1-z2)**2)
    a2=m.sqrt(b2**2+(x1-x2)**2)
    if x2<x1:
        jd2=m.acos(b2/a2)
    else:
        jd2=-m.acos(b2/a2)'''
#第三关节角度(杰诚旧电脑动捕坐标系，前y右x)
    b1=m.sqrt((x2-x3)**2+(y2-y3)**2)
    a1=m.sqrt((y2-y3)**2+b1**2)
    a3=a1
    if z3>z2:
        jd3=m.acos(b1/a3)
    else:
        jd3=-m.acos(b1/a3)
    
    #print '角度1:%s'%jd1+'角度2:%s'%jd2+'角度3:%s'%jd3
    rob.movej((2.37, -1.76, -0.5+jd3, 2.7435, 4.7691, 3.8132),5,5)  #0.3s
    b=datetime.datetime.now()
    print b-a
if __name__ == "__main__":
    rob = urx.robot.Robot("192.168.131.40")
    #x1,y1,z1,x2,y2,z2,x3,y3,z3=2,3,2,2,1,1,1,1,1
    # 初始化ROS节点 
    rospy.init_node('jiaoben', anonymous=True) 
    again = 1
    global again
    while not rospy.is_shutdown():
        MoveItIKDemo()
