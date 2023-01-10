# 爬虫项目脚本

> 数据库采用`postgresql`，运行前确保本地环境已经安装好了数据库以及相关依赖包

## 目录
```
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
- selenium
  - 下载安装包指令
    > pip install selenium==3.14 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

## 执行脚本
```bash
python manage.py runscript capture
```