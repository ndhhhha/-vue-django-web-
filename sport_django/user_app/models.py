from django.db import models
import hashlib

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ("1", '男'),
        ("0", '女'),
    )
    username = models.CharField(max_length=16, unique=True,verbose_name='用户名')
    password = models.CharField(max_length=16,verbose_name='用户密码')
    _password = models.TextField(max_length=25555,verbose_name='数据存储密码')
    nickname = models.CharField(max_length=32,verbose_name='昵称',default='默认用户')
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES,verbose_name='性别',default="1")
    introduction = models.TextField(max_length=200,verbose_name='个人简介',default='这个人很懒，什么都没有留下。')
    active_time = models.IntegerField(verbose_name='活跃时间',default=0)
    # avatar = models.ImageField(upload_to='avatar/',verbose_name='头像') 后面进行补充
    avatar = models.ImageField(upload_to='avatar/',verbose_name='头像',default='avatar/daoge.png')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    
    class Meta:
        db_table = 'sportuser'
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['-created_at']

    def __str__(self):
        return self.username
    #关于密码存储，一般服务器都会进行加密后存储。这里通过python自带的hashlib库进行加密存储。
    # 这里使用md5加密算法，当然你也可以使用sha1等其他加密算法,真实数据其实是在_password字段中存储的。
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, raw_password):
        #1、进行数据存储时，使用md5加密算法进行加密存储。
        self._password = hashlib.md5(raw_password.encode('utf-8')).hexdigest()
    #2、校验密码
    def check_password(self, raw_password):
        return self._password == hashlib.md5(raw_password.encode('utf-8')).hexdigest()