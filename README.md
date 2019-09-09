# ur5

## 1. Overview
任务：控制UR5机械臂移动和抓取
## 2. Prerequisites
### 2.1 Hardware
[Universal Robot UR5](https://www.universal-robots.com/products/ur5-robot/) Industrial Robot Arm

### 2.2 Software
Our package was developed in Ubuntu [16.04](http://releases.ubuntu.com/16.04/) and [ROS Kinetic](http://wiki.ros.org/cn/ROS/Tutorials/)[ROS Installtaion](http://wiki.ros.org/ROS/Installation).  
[MoveIt!](http://docs.ros.org/kinetic/api/moveit_tutorials/html/index.html): ROS robot planning framework  
[ur_modern_driver](https://github.com/ros-industrial/ur_modern_driver): ROS driver for UR10 robot controller from Universal Robots
### 2.3 [Test TCP/IP](http://wiki.ros.org/universal_robot/Tutorials/Getting%20Started%20with%20a%20Universal%20Robot%20and%20ROS-Industrial)

用PING命令测试通讯：  
``` 
ping IP_OF_THE_ROBOT
``` 
示例：
``` 
ping 192.168.131.40
``` 
## 3. Build on ROS
In your catkin [workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace): 
``` 
$ mkdir -p ~/ur5_ws/src

cd ~/ur5_ws/src
git clone https://github.com/iseedwyane/universal_robot.git
cd ..
catkin_make
``` 
再导入py文件，编译后run  
Note:[环境配置](http://wiki.ros.org/cn/kinetic/Installation/Ubuntu)
```
$ echo "~/ur5_ws/devel/setup.bash" >> ~/.bashrc
$ gedit .bashrc
have a look:
$ gedit .bashrc

```
## 4. Run 
### 4.1 Run in Simulation [Gazebo](http://wiki.ros.org/ur_gazebo)
#### way_1: 
1. 打开一个终端，启动Gazebo同时导入ur5的模型信息：
``` 
roslaunch ur_gazebo ur5.launch
``` 
2. 另外打开一个终端，启动moveit!的节点，并导入ur5的moveit!配置文件：
``` 
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true limited:=true
``` 
3.运行
``` 
~/ur5_ws/src/ur5_pkgby13
$ python moveit_fk_demo.py
``` 
#### way_2: 
也可以另外打开一个终端，打开可视化可交互的Rviz界面：  
``` 
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```   
在Rviz中拖动机械臂到某个位置，并选择planning>>plan，在rviz中使用MoveIt!插件选择一个运动目标姿态，然后点击“Plan”。再点击“Execute”按钮，gazebo中的UR5会按照规划的轨迹开始运动，rviz中的UR5模型保持同样的运动姿态。
#### way_3: 
``` 
rosrun ur5_pkgby13 moveit_fk_demo.py
``` 
 rosrun failed  

ssen@sen-inspiron-15-7000-gaming:~$ rosrun ur5_pkgby13 moveit_fk_demo.py  
[rosrun] Couldn't find executable named moveit_fk_demo.py below /home/ssen/ur5_ws/src/ur5_pkgby13  
[rosrun] Found the following, but they're either not files,  
[rosrun] or not executable:  
[rosrun]   /home/ssen/ur5_ws/src/ur5_pkgby13/moveit_fk_demo.py  
ssen@sen-inspiron-15-7000-gaming:~$   

### 4.2 Run with Real Robot


### 4.3 Changing execution parameters


## 5. Background

## 6. Maintenance
