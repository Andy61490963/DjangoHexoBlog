from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class homepost(models.Model):
    postname = models.CharField('Name',max_length=20)
    introduction = MDTextField('Introduction',max_length=500)
    writer = models.CharField('writer',max_length=20 ,null=True)
    website = models.URLField(max_length=250 ,blank=True ,null=True)
    post_date = models.DateTimeField(default=datetime.now ,blank=True)
    tags = models.ManyToManyField(Tag, blank=True)#tag
    ownerid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.postname


class archives(models.Model):
    postname = models.CharField('Name', max_length=20)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.postname

    def formatted_month(self):
        return self.post_date.strftime('%m')  # %m 將月份格式化為01、02、...、12的形式

    def formatted_day(self):
        return self.post_date.strftime('%d')  # %d 將日期格式化為01、02、...、31的形式


class content(models.Model):
    postname = models.CharField('Name',max_length=20)
    introduction = MDTextField('Introduction',max_length=500)
    writer = models.CharField('writer',max_length=20 ,null=True)
    website = models.URLField(max_length=250 ,blank=True ,null=True)
    post_date = models.DateTimeField(default=datetime.now ,blank=True)
    tags = models.ManyToManyField(Tag, blank=True)#tag
    ownerid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.postname