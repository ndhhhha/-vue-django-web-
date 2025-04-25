from django.db import models
from user_app.models import User

# Create your models here.
class ChatContent(models.Model):
    title = models.CharField(max_length=20, verbose_name='文章标题')
    content = models.TextField(max_length=200,verbose_name='文章内容')
    like = models.IntegerField('点赞数',default=0)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', related_name='chat_contents')

    class Meta:
        db_table = 'chat_content'
        verbose_name = '文章内容'
        verbose_name_plural = '文章内容'
        ordering = ['-created_at']

    def __str__(self):
        return self.title  
    
class Comment(models.Model):
    content = models.TextField(max_length=200,verbose_name='评论内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', related_name='user')
    chat_content = models.ForeignKey(ChatContent, on_delete=models.CASCADE, verbose_name='文章', related_name='comments')

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:20]  # 返回前20个字符作为字符串表示
    
