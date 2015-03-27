# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20150312_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='comment',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='pesit_barcode',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='ticket_category',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='ticket_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
