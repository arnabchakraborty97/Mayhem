# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20180103_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(upload_to=b'photo_file'),
        ),
    ]
