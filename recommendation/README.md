# recommendation
基于Movielens数据集的简单推荐系统实现

![模型结构](https://raw.githubusercontent.com/Aitical/recommendation/master/img/model_structure.jpg)

### 执行环境及依赖:
- Ubuntu 18.04
- Python 3.6
- jupyterlab
- pandas
- numpy

### 技术路线
- JS
- Django
- Python

### Installation

If you are using Ubuntu, you can run the command below:

```shell
git clone https://github.com/Aitical/recommendation recommendation
cd recommenddation
pip3 install -r requirements.txt
cd recommendation
python3 manage.py runserver --insecure
```

You may need sudo right to run and use  `--insecure` because in `settings.py` ,we set `ALLOWED_HOSTS = ['*']`

Now you can visit it on 'http://127.0.0.0:8000/index'

### 功能结构

- 前端交互: 提供搜索/查看/导航/推荐功能

    - 根据个人标签智能推荐

    - 模糊搜索与智能提示
    - 标签导航栏

- 推荐模型主要为两部分: 冷启动与动态更新
    - 冷启动
        - 用户初次使用时采集用户偏好标签和观影历史信息通过聚类与分类算法推荐
    - 动态更新
        - 系统采集用户使用过程中的信息,使用协同过滤矩阵,动态更新用户相关性系数进行更新推荐



