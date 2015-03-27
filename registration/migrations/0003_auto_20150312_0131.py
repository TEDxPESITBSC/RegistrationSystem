# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20150311_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='comment',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='pesit_barcode',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='ticket_category',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='ticket_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
