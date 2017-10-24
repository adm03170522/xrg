from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户
class User(AbstractUser):
    ip = models.CharField(max_length=100, verbose_name='登录IP')
    reason = models.CharField(max_length=600, verbose_name='操作原因', blank=True, null=True)
    phone_num = models.CharField(max_length=11, verbose_name='联系电话', null=False)
    comment = models.CharField(max_length=600, verbose_name='备注')

    class Meta:
        # db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(max_length=100, upload_to='banner/%Y/%m', verbose_name='轮播图')
    # url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='轮播顺序')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        # db_table = 'banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 课程
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(max_length=100, upload_to='course/%Y/%m', verbose_name='课程图片')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    # teachers = models.ForeignKey('Teacher', verbose_name='授课教师')
    category = models.ForeignKey('Category', verbose_name='所属分类')

    class Meta:
        # db_table = 'course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程分类')
    desc = models.CharField(max_length=300, verbose_name='分类描述')
    # image = models.ImageField(max_length=100, upload_to='category/%Y/%m', verbose_name='分类图片')
    icon_name = models.CharField(max_length=50, null=True, verbose_name='字体图标')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    # courses = models.ForeignKey('Course', verbose_name='包含课程')

    class Meta:
        # db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 教师
class Teacher(models.Model):
    name = models.CharField(max_length=150, verbose_name='教师名称')
    intro = models.CharField(max_length=300, verbose_name='教师简介')
    detail = models.CharField(max_length=600, verbose_name='教师详情')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    index = models.IntegerField(default=100, verbose_name='教师排序')
    course = models.ForeignKey('Course', verbose_name='所教课程')

    class Meta:
        # db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        ordering = ['index']

    def __str__(self):
        return self.name


# 客户信息
class CustomerInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='学员名称')
    age = models.IntegerField(verbose_name='年龄')
    phone_num = models.CharField(max_length=11, verbose_name='联系电话')
    comment = models.CharField(max_length=600, verbose_name='备注')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        # db_table = 'customer_info'
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
