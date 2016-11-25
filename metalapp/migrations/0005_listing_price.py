# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metalapp', '0004_auto_20150823_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
