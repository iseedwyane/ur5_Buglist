
# 到根目录下，打开终端并输入，以编辑~/.bashrc文件
```
sudo gedit ~/.bashrc
```

# 在.bashrc中添加source 要注意顺序问题，

```
source /opt/ros/kinetic/setup.bash
source ~/A/src/xxx1/devel/setup.bash
source ~/B/src/xxx2/setup.bash
source ~/new/src/xxx3/devel/setup.bash
```
即：新添加的在后面。  
或者直接用命令行添加：
```
echo 'source ~/ws_moveit/devel/setup.bash' >> ~/.bashrc
```

# 使其立即生效，在终端执行：
```
source ~/.bashrc 
```

# 查看环境变量路径配置：
```
echo $ROS_PACKAGE_PATH 
```
