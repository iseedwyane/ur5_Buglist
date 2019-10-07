
# test ip
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
# tf 
```
 roslaunch learning_tf tf_demo.launch
```


![End-effector](https://github.com/iseedwyane/ur5/blob/master/pic/ee2.png)
