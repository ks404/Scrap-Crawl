# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='weight',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='url',
            field=models.URLField(),
        ),
    ]
