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

def callback1(pose): 
    global x1,y1,z1
    x1=pose.pose.position.x
    y1=pose.pose.position.y
    z1=pose.pose.position.z
  
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
#第一关节角度
    #b1=m.sqrt((y2-y3)**2)
    #a1=m.sqrt((x2-x3)**2+b1**2)
    #if x2>x3:
        #jd1=-acos(b1/a1)
    #else:
        #jd1=acos(b1/a1)
    #print "jd1=%s"%jd1
#第二关节角度
    #b2=m.sqrt((x1-x2)**2+(z1-z2)**2)
    #a2=m.sqrt(b2**2+(y1-y2)**2)
    #if y2<y1:
        #jd2=acos(b2/a2)
    #else:
        #jd2=-acos(b2/a2)
    #print "jd2=%s"%jd2
#第三关节角度(电脑动捕坐标系)
    b3=m.sqrt((x2-x3)**2+(y2-y3)**2)
    a3=m.sqrt((z2-z3)**2+b3**2)
    global jd3
    if y3>y2:
        jd3=m.acos(b3/a3)
    else:
        jd3=-m.acos(b3/a3)
    #print "jd3=%s"%jd3

def listener(name,a):     
    pose=PoseStamped()     
    rospy.Subscriber('vrpn_client_node/RigidBody01/pose',PoseStamped,callback1)   
    rospy.Subscriber('vrpn_client_node/RigidBody02/pose', PoseStamped, callback2)
    rospy.Subscriber('vrpn_client_node/RigidBody03/pose', PoseStamped, callback3)
    rospy.spin()

def MoveItIKDemo(): 
    # 初始化ROS节点 

    rospy.init_node('zidong', anonymous=True) 
    thread.start_new_thread(listener,(1,2))
    time.sleep(0.1)
# 初始化move_group的API 

    # 

# 初始化需要使用move group控制的机械臂中的arm group 

    #arm = moveit_commander.MoveGroupCommander('manipulator') 

# 设置机械臂的允许误差值 
    #arm.set_goal_joint_tolerance(0.001)    

# 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
    joint_positions = [ 140.07/180*m.pi,-136.30/180*m.pi,-67.25/180*m.pi+jd3,145.18/180*m.pi,291.91/180*m.pi,235.74/180*m.pi] 
    arm.set_joint_value_target(joint_positions) 

    arm.go() #控制运动

    start=datetime.datetime.now()
    if arm.go() == False:
        threading.enumerate()#0.1s
    end=datetime.datetime.now()
    print(end-start)
if __name__ == "__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    arm = moveit_commander.MoveGroupCommander('manipulator')#0.8s
    arm.set_goal_joint_tolerance(0.001)
    while 1:
        MoveItIKDemo()
