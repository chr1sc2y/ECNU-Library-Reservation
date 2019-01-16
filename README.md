自动预定华东师范大学图书馆小房间单人优化版

## 使用方法
1. 克隆项目

```
git clone https://github.com/ZintrulCre/ECNU-Library-Reservation.git
```

2. 在config.json里设置你想预定的时间（最多三个）
3. 在北京时间21：00的时候在命令行中输入 python3 ECNU_Lib_Reservation.py，如果命令行提示“操作成功！”则表示预定成功

## 注意事项
- 需要[Python3](https://www.python.org/downloads/)环境
- 目前只支持预定C426
- 可以将该项目放到服务器上用crontab设置定时任务让其自动运行