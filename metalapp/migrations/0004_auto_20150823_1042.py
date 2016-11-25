# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metalapp', '0003_auto_20150823_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='weight',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
