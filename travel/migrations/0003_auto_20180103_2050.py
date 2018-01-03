# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20180103_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_caption',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.FileField(default=b'', upload_to=b''),
        ),
    ]