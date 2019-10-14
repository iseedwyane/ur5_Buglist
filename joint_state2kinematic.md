way1:moveit
# Input:/joint_state
Q1:How to input data:/joint_state  
Q2:How to input model of ur5
# Output：robot kinematics
把joint state 的数据用这个函数转为robot kinematics的xyz和q

Original：
# [api/moveit_core](http://docs.ros.org/jade/api/moveit_core/html/classmoveit_1_1core_1_1RobotState.html)
[Kinematics/C++ API](http://docs.ros.org/indigo/api/pr2_moveit_tutorials/html/kinematics/src/doc/kinematics_tutorial.html)
```
const Eigen::Affine3d & 	getGlobalLinkTransform (const std::string &link_name) const
const Eigen::Affine3d & 	getGlobalLinkTransform (const LinkModel *link) const
const Eigen::Affine3d & 	getCollisionBodyTransform (const std::string &link_name, std::size_t index) const
```
## Updating and getting transforms
# SEARCH:ur5 getGlobalLinkTransform
[MOVEIT: Compute forward kinematics and plan in Cartesian space](https://answers.ros.org/question/274093/moveit-compute-forward-kinematics-and-plan-in-cartesian-space/)

[Robot Model and Robot State](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/robot_model_and_robot_state/robot_model_and_robot_state_tutorial.html)
[MoveIt! 中的运动学模型](https://blog.csdn.net/wxflamy/article/details/79195085)

[MoveIt！入门：RobotModel、RobotState](https://blog.csdn.net/qq_26565435/article/details/90449047)

# 整理思路：

The RobotModel and RobotState classes are the core classes that give you access to a robot’s kinematics.

## The RobotModel
```
RobotModel 与 RobotState类是访问运动学的核心类。
开始设置
初始化一个RobotModelLoader对象，它将在ROS参数服务器上查找机器人描述，并构建一个RobotModel供我们使用。
robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
robot_model::RobotModelPtr kinematic_model = robot_model_loader.getModel();
ROS_INFO("Model frame: %s", kinematic_model->getModelFrame().c_str());
使用RobotModel可以构建一个RobotModel变量，保存机器人的配置信息。我们设机器人各个关节为默认值。可以得到一个JointModelGroup表示机器人的运动组，比如“right_arm”。
robot_state::RobotStatePtr kinematic_state(new robot_state::RobotState(kinematic_model));
kinematic_state->setToDefaultValues();
const robot_state::JointModelGroup *joint_model_group = kinematic_model->getJointModelGroup("right_arm");

const std::vector<std::string> &joint_names = joint_model_group->getVariableNames();
[原文链接](https://blog.csdn.net/wxflamy/article/details/79195085)
```

## RobotState

```
获得关节值
std::vector<double> joint_values;
kinematic_state->copyJointGroupPositions(joint_model_group, joint_values);
for (std::size_t i = 0; i < joint_names.size(); ++i)
{
  ROS_INFO("Joint %s: %f", joint_names[i].c_str(), joint_values[i]);
关节限制
/* Set one joint in the right arm outside its joint limit */
joint_values[0] = 1.57;
kinematic_state->setJointGroupPositions(joint_model_group, joint_values);

/* Check whether any joint is outside its joint limits */
ROS_INFO_STREAM("Current state is " << (kinematic_state->satisfiesBounds() ? "valid" : "not valid"));

/* Enforce the joint limits for this state and check again*/
kinematic_state->enforceBounds();
ROS_INFO_STREAM("Current state is " << (kinematic_state->satisfiesBounds() ? "valid" : "not valid"));
正向运动学
通过一组随机的关节值实现正向运动学。

kinematic_state->setToRandomPositions(joint_model_group);
const Eigen::Affine3d &end_effector_state = kinematic_state->getGlobalLinkTransform("r_wrist_roll_link");

/* Print end-effector pose. Remember that this is in the model frame */
ROS_INFO_STREAM("Translation: " << end_effector_state.translation());
ROS_INFO_STREAM("Rotation: " << end_effector_state.rotation());
```
### setJointGroupPositions
[moveit::core::RobotState Class Reference](http://docs.ros.org/kinetic/api/moveit_core/html/classmoveit_1_1core_1_1RobotState.html#aba31c6f758e3dabd32c1acbd069e189e)
### joint_model_group
[moveit::core::JointModelGroup Class Reference](http://docs.ros.org/indigo/api/moveit_core/html/classmoveit_1_1core_1_1JointModelGroup.html)
[robot_state.h](http://docs.ros.org/jade/api/moveit_core/html/robot__state_8h_source.html)



# PR2:PERSONAL ROBOT 2


way2:[urx](https://zhuanlan.zhihu.com/p/41944197)
