from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    models.AutoField(primary_key=True)
    blogName = models.CharField(max_length=30, verbose_name="博客名", blank=True)
    blogType = models.CharField(max_length=20, verbose_name="博客类型", blank=True)
    blogPublishTime = models.DateTimeField(verbose_name="博客发表时间", default=timezone.now)
    blogAuthor = models.CharField(max_length=30, verbose_name="博客发表人")
    blogLink = models.CharField(max_length=30, verbose_name='博客所在位置', blank=True)

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name