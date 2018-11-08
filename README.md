# recommenddation
基于Movielens数据集的简单推荐系统实现
-------
### 执行环境及依赖:
- Ubuntu 18.04
- Python 3.6
- jupyterlab
- pandas
- numpy

### 技术路线:
- JS
- Django
- Python

### 项目特色 
- 待完成

### 功能结构

- 前端交互: 提供搜索/查看/导航/推荐功能
    -待完成

- 推荐模型主要为两部分: 冷启动与动态更新
    - 冷启动
        - 用户初次使用时采集用户偏好标签和观影历史信息进行分类算法推荐
    - 动态更新
        - 系统采集用户使用过程中的信息,使用协同过滤矩阵,动态更新用户相关性系数进行更新推荐

### 安装使用

before execute the command next, you should confirm the environment we need

```shell
git clone https://github.com/Aitical/recommenddation recommenddation
cd recommenddation
python3 manage.py runserver
```

and you can use it on 'http://127.0.0.0:8000'

