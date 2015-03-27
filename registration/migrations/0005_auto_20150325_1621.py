# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20150312_0136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='got_goodies_bag',
            new_name='got_goodie_bag',
        ),
    ]
