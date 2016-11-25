# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metalapp', '0002_auto_20150823_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
