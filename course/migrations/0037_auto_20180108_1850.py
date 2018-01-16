# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-08 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0036_auto_20170907_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinstance',
            name='index_mode',
            field=models.IntegerField(choices=[(0, 'User results'), (1, 'Table of contents'), (2, 'Link to last visited content'), (10, 'Experimental setup (hard-coded)')], default=0, help_text='Select content for the course index page.'),
        ),
        migrations.AlterField(
            model_name='usertag',
            name='description',
            field=models.CharField(blank=True, help_text='Describe the usage or meaning of this usertag.', max_length=164),
        ),
    ]