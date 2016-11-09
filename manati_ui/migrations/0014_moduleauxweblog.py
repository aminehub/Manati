# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0013_appparameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleAuxWeblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('status', models.CharField(choices=[('seed', 'seed'), ('modified', 'modified'), ('undefined', 'undefined')], default='undefined', max_length=20)),
                ('weblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manati_ui.Weblog')),
            ],
            options={
                'db_table': 'manati_module_aux_weblogs',
            },
        ),
    ]