# -*- coding: utf-8 -*-
#  Copyright (c) 2021-2022 THL A29 Limited
#  #
#  This source code file is made available under MIT License
#  See LICENSE for details
#  ==============================================================================
# Generated by Django 3.1.14 on 2022-07-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20220729_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='ext_field',
            field=models.JSONField(blank=True, null=True, verbose_name='扩展字段'),
        ),
    ]
