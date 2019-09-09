# [Robotiq](https://github.com/GJXS1980/Lab409_RUR/blob/master/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%8F%B0%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8BV3.0.md)
```
#安装soem
sudo apt-get install ros-$ROS_DISTRO-soem

#下载并编译robotiq功能包
mkdir -p ~/robotiq_ws/src && cd ~/robotiq_ws/src
git clone https://github.com/GJXS1980/Lab409_Robotiq.git
cd ~/robotiq_ws && catkin_make

echo "export robotiq_ws='$(pwd)'" >> ~/.bashrc
echo "source $(pwd)/devel/setup.bash" >> ~/.bashrc
bash

rosdep install robotiq_modbus_tcp
```
[GJXS1980/Lab409_Robotiq](https://github.com/GJXS1980/Lab409_Robotiq)
