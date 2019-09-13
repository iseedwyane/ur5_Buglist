import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand

def talker_by13():

    moveit_commander.roscpp_initialize(sys.argv)

    rospy.init_node('moveit_fk_demo')
 

    arm = moveit_commander.MoveGroupCommander('manipulator')     
    arm.set_goal_joint_tolerance(0.001)


    joint_positions = [1, -1.9, 1, 1.49,1.886, -2.128]
    #joint_positions = [0, 0, 0, 0,0, 0]
    arm.set_joint_value_target(joint_positions)
                 

    arm.go()
    rospy.sleep(1)
        

    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        talker_by13()
    except rospy.ROSInterruptException:
        pass
