# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_comment_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['posted_on']},
        ),
    ]