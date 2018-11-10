from django.db import models

# Create your models here.


class Item_msg(models.Model):
    """
    电影信息表
    """
    item_id = models.IntegerField(null=False)
    title = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=100, null=False)
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=2)
    times = models.IntegerField(default=0)
    hot_point = models.IntegerField(default=0)
    label = models.CharField(default='0', max_length=20)

    def __str__(self):
        return self.title


class Item_labels(models.Model):
    """
    电影标签表
    """
    label = models.CharField(max_length=10)


class Item_label(models.Model):
    """
    电影分类列表
    """
    item_id = models.IntegerField(null=False)
    label = models.IntegerField(null=False)


class User_label(models.Model):
    """
    用户分类列表
    """
    user_id = models.IntegerField(null=False)
    label = models.IntegerField(null=False)


class User_item(models.Model):
    """
    用户到电影
    """
    user_id = models.IntegerField(null=False)
    item_id = models.IntegerField(null=False)

    def __str__(self):
        return self.user_id

