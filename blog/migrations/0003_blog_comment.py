# Generated by Django 3.1 on 2020-08-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
