#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import numpy
import math
from math import pi 
import thread
import threading
import time

def callback(pose): 
#获取标记点位姿和位置
    global x,y,z,qx,qy,qz,qw
    x=pose.pose.position.x
    y=pose.pose.position.y
    z=pose.pose.position.z
    qx=pose.pose.orientation.x
    qy=pose.pose.orientation.y
    qz=pose.pose.orientation.z
    qw=pose.pose.orientation.w

def callback1(pose): 
#获取移动平台基座位姿和位置
    global x1,y1,z1,qx1,qy1,qz1,qw1
    x1=pose.pose.position.x
    y1=pose.pose.position.y
    z1=pose.pose.position.z
    qx1=pose.pose.orientation.x
    qy1=pose.pose.orientation.y
    qz1=pose.pose.orientation.z
    qw1=pose.pose.orientation.w
    
def listener(name,a):  
    #rospy.init_node('dong', anonymous=True)
    #rate=rospy.Rate(10)     
    pose=PoseStamped()     
    rospy.Subscriber('vrpn_client_node/RigidBody/pose', PoseStamped, callback)  
    rospy.Subscriber('vrpn_client_node/RigidBody002/pose', PoseStamped, callback1)
    rospy.spin()

def MoveItIkDemo():
    rospy.init_node('dong', anonymous=True)
    thread.start_new_thread(listener,(1,2))
    global x1,y1,z1,qx1,qy1,qz1,qw1
    global x,y,z,qx,qy,qz,qw
    again = 1
    while again:
        time.sleep(0.5)
        again = 0
    m=x1-x
    n=y1-y
    o=z1-z
    #print 'm=%f'%m
    # 初始化move_group的API
    moveit_commander.roscpp_initialize(sys.argv)
    
    # 初始化ROS节点
    #rospy.init_node('moveit_ik_demo')
            
    # 初始化需要使用move group控制的机械臂中的arm group
    arm = moveit_commander.MoveGroupCommander('manipulator')
            
    # 获取终端link的名称
    end_effector_link = arm.get_end_effector_link()
                    
    # 设置目标位置所使用的参考坐标系
    reference_frame = 'base_link'
    arm.set_pose_reference_frame(reference_frame)
            
    # 当运动规划失败后，允许重新规划
    arm.allow_replanning(True)
    
    # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
    arm.set_goal_position_tolerance(0.01)
    arm.set_goal_orientation_tolerance(0.05)
    
    # 控制机械臂先回到初始化位置
   
           
    # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
    # 姿态使用四元数描述，基于base_link坐标系
	
    target_pose = PoseStamped()
    target_pose.header.frame_id = reference_frame
    target_pose.header.stamp = rospy.Time.now()     
    target_pose.pose.position.x = m
    target_pose.pose.position.y = n
    target_pose.pose.position.z = o
    target_pose.pose.orientation.x = qx1
    target_pose.pose.orientation.y = qy1
    target_pose.pose.orientation.z = qz1
    target_pose.pose.orientation.w = qw1
    #for i in range(1):
    # 设置机器臂当前的状态作为运动初始状态
    arm.set_start_state_to_current_state()
    
    # 设置机械臂终端运动的目标位姿
    arm.set_pose_target(target_pose, end_effector_link)
    
    # 规划运动路径
    traj = arm.plan()
    
    # 按照规划的运动路径控制机械臂运动
    arm.execute(traj)
    if arm.execute(traj) == False:
        threading.enumerate()

if __name__ == "__main__":
    while 1:
        MoveItIkDemo()
    #while 1: 
        #print "before"    

      
        
        #rospy.sleep(3)
        #ik+=1
        #print "ik=%f"%ik

    
