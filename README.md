# ECNU Library Reservation

自动预定华东师范大学图书馆小房间

## 使用方法
1. 克隆项目

```
git clone https://github.com/ZintrulCre/ECNU-Library-Reservation.git
```

2. 在reservations文件夹下新建多个json文件，在文件里按照reservations_template.json的格式设置预定的时间
3. 在北京时间21：00的时候在命令行中输入 python3 ECNU_Lib_Reservation.py，如果命令行提示“操作成功！”则表示预定成功

## 注意事项
- 需要[Python3](https://www.python.org/downloads/)环境
- 只支持预定C426和C413
- 可以放到服务器上用crontab设置定时任务自动运行
