# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0007_dont_filter_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=2000, blank=True)),
                ('weight', models.DecimalField(max_digits=6, decimal_places=2, blank=True)),
                ('location', models.CharField(max_length=2000, blank=True)),
                ('closing', models.CharField(max_length=2000, blank=True)),
                ('link', models.CharField(max_length=2000, blank=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=2000, blank=True)),
                ('url', models.CharField(max_length=2000, blank=True)),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
                ('scraper_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='search_term',
            field=models.ForeignKey(to='metalapp.SearchTerm'),
        ),
    ]
