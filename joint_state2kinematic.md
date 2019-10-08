way1:moveit
# Input:/joint_state
# Output：robot kinematics
把joint state 的数据用这个函数转为robot kinematics的xyz和q

Original：
# [api/moveit_core](http://docs.ros.org/jade/api/moveit_core/html/classmoveit_1_1core_1_1RobotState.html)

```
const Eigen::Affine3d & 	getGlobalLinkTransform (const std::string &link_name) const
const Eigen::Affine3d & 	getGlobalLinkTransform (const LinkModel *link) const
const Eigen::Affine3d & 	getCollisionBodyTransform (const std::string &link_name, std::size_t index) const
```
# SEARCH
[MOVEIT: Compute forward kinematics and plan in Cartesian space](https://answers.ros.org/question/274093/moveit-compute-forward-kinematics-and-plan-in-cartesian-space/)

[Robot Model and Robot State](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/robot_model_and_robot_state/robot_model_and_robot_state_tutorial.html)
[MoveIt! 中的运动学模型](https://blog.csdn.net/wxflamy/article/details/79195085)














way2:[urx](https://zhuanlan.zhihu.com/p/41944197)
