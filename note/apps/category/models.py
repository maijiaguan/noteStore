from django.db import models


class Category(models.Model):
    """
    标签
    """
    category_name = models.CharField(max_length=10, verbose_name="标签名", default='未命名')
    category_color = models.CharField(max_length=10, verbose_name="标签颜色", default='#db0036')
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='user_category')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name

