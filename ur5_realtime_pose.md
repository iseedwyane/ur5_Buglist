
# [test ip](https://answers.ros.org/question/324950/ur3-connection-setup-failed-ur_modern_driver/);[Config](https://github.com/GJXS1980/Lab409_RUR/blob/master/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%8F%B0%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8BV3.0.md)
```
sudo gedit /etc/hosts
```
my PC_ip=192.168.131.39
# enable the ur5
initialize ur5 on controller 
# connect 
```
 roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=192.168.131.40 [reverse_port:=REVERSE_PORT]
```
# moveit config
```
 roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch

```
# rviz
```
roslaunch ur5_moveit_config moveit_rviz.launch config:=true

```
# camera 
```
roslaunch aruco_ros single_realsense.launch
rostopic echo /aruco_single/pose
```




# tf 
```
 roslaunch learning_tf tf_demo.launch
```

![End-effector](https://github.com/iseedwyane/ur5/blob/master/pic/ee2.png)

```
rqt_graph
rostopic echo /tf_static
rosrun tf view_frames 
```
![base2end2cam2aruco](https://github.com/iseedwyane/ur5/blob/master/pic/2019-10-07%20suc3.png)
