# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyApp', '0004_auto_20170221_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
