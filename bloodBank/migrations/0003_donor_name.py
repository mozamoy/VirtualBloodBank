# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodBank', '0002_blocked_list_blood_seeker'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
