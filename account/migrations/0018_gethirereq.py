# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20171221_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gethirereq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email_id', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=250)),
                ('remark', models.CharField(max_length=500)),
                ('req_time', models.DateTimeField(auto_now_add=True)),
                ('gethire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Gethired')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
