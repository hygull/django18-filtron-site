# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyApp', '0008_auto_20170303_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text=b'width should be >= 1200 and height should be >= 800. 1200x800 resolution or greater is ok', upload_to=b''),
        ),
    ]
