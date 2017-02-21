# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyApp', '0003_auto_20170221_1536'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AuthUser',
        ),
    ]
