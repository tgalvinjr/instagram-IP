# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20190521_0549'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InstagramRecepients',
        ),
    ]
