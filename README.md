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

#### 安装MoveIt
```
sudo apt-get install ros-kinetic-moveit-*
```
### 
```
sudo apt install ros-kinetic-ur-*
sudo apt install ros-kinetic-ur5-moveit-config 

```

### 2.3 [Test TCP/IP](http://wiki.ros.org/universal_robot/Tutorials/Getting%20Started%20with%20a%20Universal%20Robot%20and%20ROS-Industrial)
[Set PC_ip](https://github.com/GJXS1980/Lab409_RUR/blob/master/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%8F%B0%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8BV3.0.md)
 

#### Run with real robot 用PING命令测试通讯：  
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
$ mkdir -p ur5_ws/src

cd ~/ur5_ws/src
git clone https://github.com/iseedwyane/universal_robot.git
cd ..
catkin_make
``` 
再导入py文件，编译后run  
Note:[环境配置](http://wiki.ros.org/cn/kinetic/Installation/Ubuntu)
```

echo "source ~/ur5_ws/devel/setup.bash" >> ~/.bashrc
source ~/.zbarc
---------------
$ echo "~/ur5_ws/devel/setup.bash" >> ~/.bashrc
$ source .bashrc 
have a look:
$ gedit .bashrc
$ sudo gedit .bashrc

```
查看路径配置结果：
```
echo $ROS_PACKAGE_PATH 
```
## 4. Run 
### 4.0.1Run in Gazebo and Rviz:
```
$ roslaunch ur_gazebo test2.launch simulation:=true

```
### 4.0.2 Run aruco_realsense
```
$ roslaunch aruco_ros single_realsense.launch
```
```
rqt_image_view 
rostopic echo /aruco_single/pose
```
### 4.0.3 Run tf
```
roslaunch learning_tf tf_demo.launch
```

### 4.1 Run in Simulation [Gazebo](http://wiki.ros.org/ur_gazebo)
#### way_final
1. 打开一个终端，启动Gazebo同时导入ur5的模型信息：
``` 
PC:$ roslaunch ur_gazebo test.launch simulation:=true
roslaunch ur_gazebo test2.launch simulation:=true
```  
2.运行
``` 
$ ~/ur5_ws/script
$ python test_demo.py   &&  test_demo2.py   
python cartesian3_succ.py
```  
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
Put these launch commander into test2.launch file in ur_gazebo package
```
roslaunch ur_gazebo test2.launch
```
is also ok.

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
