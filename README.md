# 爬虫项目脚本

> 数据库采用`mysql`，运行前确保本地环境已经安装并创建好了数据库以及相关依赖包

## 目录
```
    |-- capture          capture app
    |-- capture_script  
        |-- settings.py  项目设置入口文件
    |-- scripts
        |-- capture.py   爬虫脚本入口文件
    |-- manage.py
    |-- README.md        自述文件
```

## 依赖包
- django
- psycopg2
- django-extensions
- pymysql
- selenium
  - 下载安装包指令
    > pip install selenium==3.14 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

## 执行脚本
运行脚本前先进行数据库迁移
```bash
python manage.py makemigrations
python manage.py manage
```

运行脚本
```bash
python manage.py runscript capture
```