

```
ssen@sen-inspiron-15-7000-gaming:~/moveit_ws$ catkin build
```
BUG:
```
Errors     << moveit_tutorials:make /home/ssen/moveit_ws/logs/moveit_tutorials/build.make.000.log
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake): 
/usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/usr/bin/cmake: /usr/local/curl/lib/libcurl.so.4: no version information available (required by /usr/bin/cmake)
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_setopt@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_perform@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_init@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_init@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_cleanup@CURL_OPENSSL_3’未定义的引用
collect2: error: ld returned 1 exit status
make[2]: *** [/home/ssen/moveit_ws/devel/.private/moveit_tutorials/lib/moveit_tutorials/robot_model_and_robot_state_tutorial] Error 1
make[1]: *** [doc/robot_model_and_robot_state/CMakeFiles/robot_model_and_robot_state_tutorial.dir/all] Error 2
make[1]: *** 正在等待未完成的任务....
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_setopt@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_perform@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_init@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_init@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_setopt@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_init@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_perform@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_init@CURL_OPENSSL_3’未定义的引用
collect2: error: ld returned 1 exit status
collect2: error: ld returned 1 exit status
make[2]: *** [/home/ssen/moveit_ws/devel/.private/moveit_tutorials/lib/moveit_tutorials/ros_api_tutorial] Error 1
make[2]: *** [/home/ssen/moveit_ws/devel/.private/moveit_tutorials/lib/moveit_tutorials/planning_scene_tutorial] Error 1
make[1]: *** [doc/kinematics/CMakeFiles/ros_api_tutorial.dir/all] Error 2
make[1]: *** [doc/planning_scene/CMakeFiles/planning_scene_tutorial.dir/all] Error 2
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_setopt@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_init@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_cleanup@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_easy_perform@CURL_OPENSSL_3’未定义的引用
/opt/ros/kinetic/lib/libresource_retriever.so：对‘curl_global_init@CURL_OPENSSL_3’未定义的引用
collect2: error: ld returned 1 exit status
make[2]: *** [/home/ssen/moveit_ws/devel/.private/moveit_tutorials/lib/moveit_tutorials/planning_scene_ros_api_tutorial] Error 1
make[1]: *** [doc/planning_scene_ros_api/CMakeFiles/planning_scene_ros_api_tutorial.dir/all] Error 2
make: *** [all] Error 2
cd /home/ssen/moveit_ws/build/moveit_tutorials; catkin build --get-env moveit_tutorials | catkin env -si  /usr/bin/make --jobserver-fds=6,7 -j; cd -
...............................................................................
Failed     << moveit_tutorials:make                [ Exited with code 2 ]      
Failed    <<< moveit_tutorials                     [ 28.9 seconds ]            
[build] Summary: 2 of 3 packages succeeded.                                    
[build]   Ignored:   None.                                                     
[build]   Warnings:  3 packages succeeded with warnings.                       
[build]   Abandoned: None.                                                     
[build]   Failed:    1 packages failed.                                        
[build] Runtime: 35.0 seconds total.                                           
[build] Note: Workspace packages have changed, please re-source setup files to use them.


```


# 定位一下 libcurl 的位置：
```
locale libcurl.so.4
```
得到：
```
ssen@sen-inspiron-15-7000-gaming:~$ locale libcurl.so.4
locale: 不明名称 “libcurl.so.4”
```



