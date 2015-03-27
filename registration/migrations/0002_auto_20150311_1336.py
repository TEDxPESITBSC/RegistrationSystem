# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='date_registered',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
