# [link](https://zhuanlan.zhihu.com/p/77905195)

使用 $ date 命令再次检查时区是否已真正更改：  
```
$ date
Tue Jul 30 20:22:33 CST 2019
```
CST（中国标准时间）
[UTC](https://baike.baidu.com/item/%E5%8D%8F%E8%B0%83%E4%B8%96%E7%95%8C%E6%97%B6/787659?fromtitle=UTC&fromid=5899996&fr=aladdin)
要切换回 UTC 时区，只需运行：
```
$ sudo timedatectl set-timezone UTC
```
在较旧的 Ubuntu 版本中，没有 timedatectl 命令。这种情况下，可以使用 tzdata（Time zone data）来设置时间同步。
```
$ sudo dpkg-reconfigure tzdata
```
