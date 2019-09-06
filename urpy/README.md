
# import
```
import rospy, sys  
```
[rospy](http://wiki.ros.org/rospy/Tutorials)
如果要写ROS节点，需要导入rospy。 
```
import moveit_commander  
```
```
from control_msgs.msg import GripperCommand  
```
control_msgs.msg的目的是可以使用control_msgs/String消息类型来发布  

# class
```
class MoveItFkDemo:  
    def __init__(self):  
```
关于Python的类别(Class)Example:  
(知识点)[如何理解python的类与对象？](https://www.zhihu.com/question/27699413)
```
class Animal(): 
def __init__(self, name): 
  self.name = name 
a = Animal("dog") #建立一个名叫dog的Animal实体(物件) 
print(a.name)
```
## [First initialize moveit_commander and rospy. ](http://docs.ros.org/indigo/api/pr2_moveit_tutorials/html/planning/scripts/doc/move_group_python_interface_tutorial.html)
```
        moveit_commander.roscpp_initialize(sys.argv)   #初始化move_group的API 
        rospy.init_node('moveit_fk_demo', anonymous=True)   #初始化ROS节点
 ```
 
[Initialize the move group for the ur5_arm]
```
        arm = moveit_commander.MoveGroupCommander('manipulator') #初始化需要使用move group控制的机械臂中的arm group
        #gripper = moveit_commander.MoveGroupCommander('endeffector')#初始化需要使用move group控制的机械臂中的gripper group
```        

```
        arm.set_goal_joint_tolerance(0.001) #设置机械臂和夹爪的允许误差值
        #gripper.set_goal_joint_tolerance(0.001)
```
         
设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
```        
        joint_positions = [1, -1.9, 1, 3.49,4.886, -2.128]
        arm.set_joint_value_target(joint_positions)
 ```                
控制机械臂完成运动
 ```       
        arm.go()
        rospy.sleep(1)
 ```
关闭并退出moveit
 ```

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
```

```
if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
 ```
