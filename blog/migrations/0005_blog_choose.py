# Generated by Django 3.1 on 2020-08-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_last_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='choose',
            field=models.IntegerField(default=1),
        ),
    ]
