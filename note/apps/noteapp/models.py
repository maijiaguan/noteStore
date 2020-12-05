import uuid
from django.db import models


# Create your models here.
class Notes(models.Model):
    """
    笔记信息
    """
    note_uid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    note_title = models.CharField(max_length=50, blank=True, verbose_name="标题", default='未命名')
    note_last_time = models.DateField(blank=True, auto_now=True, verbose_name="最新编辑时间")
    note_content_v1 = models.TextField(blank=True, null=True, verbose_name="笔记v1")
    note_content_v2 = models.TextField(blank=True, null=True, verbose_name="笔记v2")
    note_content_v3 = models.TextField(blank=True, null=True, verbose_name="笔记v3")
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='user_notes')
    folder = models.ForeignKey('NotesFolder', on_delete=models.CASCADE, null=True, related_name='folder_notes')
    category = models.ForeignKey('category.Category', on_delete=models.SET_NULL, null=True, related_name='category_notes')

    class Meta:
        ordering = ['-note_last_time']
        verbose_name = "笔记信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.note_title


class NotesFolder(models.Model):
    """
    笔记本
    """
    folder_uid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    folder_name = models.CharField(max_length=30, verbose_name="标签名", default='未命名')
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='user_folder')
    category = models.ForeignKey('category.Category', on_delete=models.SET_NULL, null=True, related_name='category_folder')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.folder_name

