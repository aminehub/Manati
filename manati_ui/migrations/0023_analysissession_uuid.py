# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-06 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0022_weblog_was_whois_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysissession',
            name='uuid',
            field=models.CharField(default='', max_length=40, null=True),
        ),
    ]
