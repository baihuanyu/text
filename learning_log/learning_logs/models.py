from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    '''用户学习主题'''
    text = models.CharField(max_length=200)# 主题字符不超过200字符
    date_added = models.DateTimeField(auto_now_add=True)#设置添加日期
    #关联用户外链  主题是最大的 只需要在最大的上面关联 主题下面的自动关联
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text

class Entry(models.Model):
    '''学习到某个主题的内容'''
    topic = models.ForeignKey(Topic)# 关联主题
    text = models.TextField()# 文本信息
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'# 此方法用于管理多个项目 如果没有 就是Entry来管理

    def __str__(self):
        return  self.text[:50] +'......'