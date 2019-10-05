roslaunch工具是ros中python实现的程序启动工具，通过读取launch文件中的参数配置、属性配置等来启动一系列节点；
很多ROS包或源码包中都有launch文件，一般为该程序包能够运行起来的基本demo配置,运行下面指令自动补全会提示该包现有的launch文件:
$roslaunch  package_name  file.launch
launch文件的位置并不是很重要，如果放在任意一个位置，可以运行下面指令:
$roslaunch  path-to-where/file.launch

launch文件是XML格式标记文本,后缀名无关紧要，一般为.launch/.xml/.test/无后缀
最简单的配置如下：
<launch>
  <node name="you_define_node_name" pkg="package_name" type="exe_name" />
</launch>
启动上面的launch文件就会启动package_name包下的exe_name执行文件,you_define_node_name自定义的node_name

<launch> tag是launch文件根元素/根标签，其他标签包含在其中，/标志结束，多行时标签tag成对存在可以包含其他标签



一个复杂的配置：
<launch>
    <!-- comment注释  -->
    
     <!-- arg can be set from high level like this  -->
    <!-- this is the include launch file content:
        <launch>
          <!-- declare arg to be passed in -->
          <arg name="arg_2" /> 

          <!-- read value of arg -->
          <param name="param_2" value="$(arg arg_2)"/>
        </launch>
    -->
    <include file="$(find pkg_name)/path-to/included.launch" ns="namespace">   
        <!-- pass value from high level to included.launch -->
        <arg name="arg_2"  value="value" />
    </include>
    
    <arg name="arg_3"  default="value" />
    <arg name="arg_4"  value="value" />
    
    <node pkg="pkg_name" type="exe_name" name="node_name1" args="arg1 arg2 arg3" respawn="true" output="screen">  
      
         <rosparam command="load" file="$(find pkg_name)/example.yaml"/>

        <param name="frame_id" value="$(arg frame_id)"/>
    </node>   
    <node pkg="pkg_name" type="exe_name" name="node_name2" args="arg1 arg2 arg3" respawn="true" output="screen">  
      
        <param name="name1" type="double" value="10.0"/>
        <param name="name2" value="$(arg arg_1)"/>
        <param name="name3" value="$(env ENVIRONMENT_VARIABLE_NAME)"/>
        <param name="name4" command="$(find pkg_name)/path-to/exe '$(find pkg_name)/path-to/arg.txt'"/>


        <remap from="laser_topic" to="/scan"/>
        <remap from="base_link" to="$(arg arg_1)"/>
    </node>    
    <group if="$(arg use_rviz)">
      <node pkg="rviz" type="rviz" name="rviz" 
            args="-d $(find pkg_name)/launch/VLP16_2D.rviz"/>
    </group>
</launch>
上面的launch文件首先声明了一些参数，之后include另一个launch文件，included.launch文件中的节点会按深度优先执行配置和启动；
之后该launch文件启动3个节点，前两个节点来自同一个包的同一个可执行文件，节点命名不能相同，每个节点可以进行自己的参数配置；
之后该launch文件启动rviz节点，参数传递 rviz的配置文件，不同配置用于显示不同的信息
<group>可以作为一组标签的容器，从而使该组有独立的名称空间
所以标签可使用 if/unless属性，如果条件成立则包含标签

launch常用标签tag：
<arg> 参数声明，arg_1 通过命令行传递，arg_2 传递到included.launch， arg_3 默认值可以被重写覆盖，agr_4不能被重写

<include> 包含其他文件，包含文件中定义的参数、变量、节点都会按深度优先遍历依次执行生效

<param>：设置变量到参数服务器,参数服务器的概念看ros wiki

<rosparam>: dump/load、delete parameters from/to  Parameter Server,常用来加载程序的参数配置文件到参数服务器，然后程序从参数服务器取得参数值；

<remap>:名称映射 from:被映射名称 to:目标名称,名称映射的概念看ros wiki

<node> 启动节点,
    <node>常用属性tag:
    pkg:"pkg_name"  包名
    type:"exe_name"  节点类型，即编译生成的可执行文件
    name:"node_name" 节点名称，自定义但不能重复
    args:"arg1 ..."  传递节点的参数列表
    respawn:"true" 如果节点退出自动重启 default：false
    output:"screen" 标准输出/标准错误输出重定向屏幕，log重定向log文件，default:log
    required:"true" 如果节点退出，杀死全部launch进程
    launch-prefix:"prefix arguments" 前置的参数，可以使用其他工具如gdb,valgrind等

    <node>常用标签tag:
    param
    remap
    rosparam

    lannch机制不保证节点的启动顺序，虽然launch文件是顺序分析，但节点初始化的时间长度不一，启动时间不一
</node>

​ 1 .launch文件的结构

            <launch>

                       <node name="talker"pkg="rospy_tutorials" type="talker" >

                        </node>​

            </launch>

      上面是.launch文件的最小例子。.launch文件开头是以<launch>​为标签，让我们知道这是一个.launch文件，以</launch>为结尾。而中间就是写自己要启动的节点，是以<node> 开始，</node>结束，其中pkg="rospy_tutorials"，这是自己要启动的节点所在的包；type="talker"，这是自己写的节点.cpp程序通过编译生产的可执行文件的名字，你最初编译.cpp程序的时候要在CMakeLists.txt添加cpp程序编译的设置，这个可执行文件的名字在CMakeLists.txt中就可以找到；name="talker"，这是节点的名字。

2.Roslaunch /XML/remap     ​

 1. 元素​

<node> 启动一个节点.

<param> 设置参数服务器上的参数

<remap> 声明一个名称的映射，允许你通过名称映射参数到ROS 节点（通过更结构化的方式而不是直接设置节点参数属性来启动的节点）。

<machine> 声明启动要使用的机器.

<rosparam> 使用rosparam 文件设置启动要用的ROS 参数

<include> 包含roslaunch 文件.

<env> 制定启动节点的环境变量

<test> 启动一个测试节点see rostest).

<arg> 声明参数

<group> 共享一个命名空间或映射的封闭的元素组。

2 .launch文件的重映射（remap）​

       据我理解，重映射就是甲节点得到相关的信息，通过重映射使乙节点得到甲节点一样的信息，从而使得乙节点模仿甲节点做出相应的响应。​

<remap>标签适用于在其范围内随后的所有声明(<launch>, <node> or<group>)。

准备工作

​需要用到rqt和tuetlesim 这两个包．如果没有安装，请执行：

$ sudo apt-get install ros-hydro-rqtros-hydro-rqt-common-plugins ros-hydro-turtlesim

我的ros版本是hydro版本，如果不是hydro，则自行替换。​

 

launch
在ROS应用中，每个节点通常有许多参数需要设置，为了方便高效操作多个节点，可以编写launch文件，然后用roslaunch命令运行
roslaunch: roslaunch [options] [package] <filename> [arg_name:=value...]
                    roslaunch [options] <filename> [<filename>...] [arg_name:=value...]
launch文件的一般格式，参数：
<launch>
    <node .../>
    <rosparam ..../>
    <param .../>
    <include .../>
    <env .../>
    <remap .../>
    <arg.../>
</launch>

 

参数说明
<node >要启动的node参数
    pkg=''mypackage''
    type=''nodetype''
    name=''nodename''
    arg=''arg1 ....''(可选)
    respawn=''ture''(可选)如果节点停止，自动重启节点
    ns=''foo''（可选）在foo命名空间启动节点
    output=''log|screen''(可选)
<rosparam>操作yaml文件参数
    command=''load|dump|delete''(默认load)
    file=''$(find pkg-name)/path/foo.yaml''(load或dump命令)yaml文件的名字
    param=''param-name''参数名
<param>定义一个设置在参数服务器的参数，它可以添加到<node>中
    name=''namespace/name''
    value=''value''（可选）如果省略这个参数，则应指定一个文件(binfile/textfile)或命令
    type=''str|int|double|boot''(可选)指定参数的类型
    textfile=''$(find pkg-name)/path/file''(可选)   

    binfile=''$(find pkg-name)/path/file''()
    command=''(find pkg-name)/exe '$(find pkg-name)/arg.txt' ''(可选)exe是可执行文件（cpp、py），arg.txt是参        数文件
<include>在当前launch文件中调用另一个launch文件
    file=''$(find pkg-name)/path/launch-file.launch''    
<env>设置节点的环境变量
    name=''environment-variable-name''
    value=''environment-variable-value''    
<remap>将一个参数名映射为另一个名字
    from=''original-name''
    to=''new-name''    
<arg>定义一个局部参数，该参数只能在一个launch文件中使用
    <arg name=''foo''/>声明一个参数foo，后面需要给它赋值
    <arg name=''foo'' default=''1''/>声明一个参数foo，如不赋值取默认值
    <arg name=''foo'' value=''bar''/>声明一常量foo，它的值不能修改
