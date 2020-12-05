import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    """
    用户表（继承AbstractUser）
    """
    user_uid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(blank=True, verbose_name="用户头像", null=True)
    mobile = models.CharField(max_length=11, verbose_name="手机号", unique=True)

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Code(models.Model):
    """
    验证码
    """
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    code = models.CharField(max_length=6, verbose_name='验证码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    end_time = models.DateTimeField(default=datetime.now, verbose_name='过期时间')

    class Meta:
        verbose_name = '验证码表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mobile

