# Generated by Django 3.2 on 2021-07-25 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_blogpublishtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogLink',
            field=models.CharField(blank=True, max_length=30, verbose_name='博客所在位置'),
        ),
    ]
