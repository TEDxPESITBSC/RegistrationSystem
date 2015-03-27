# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_registered', models.DateField()),
                ('attendee_name', models.CharField(max_length=200)),
                ('attendee_email', models.EmailField(max_length=75)),
                ('ticket_name', models.CharField(max_length=100)),
                ('ticket_category', models.CharField(max_length=100)),
                ('order_number', models.CharField(max_length=100)),
                ('ticket_number', models.CharField(max_length=100)),
                ('buyer_name', models.CharField(max_length=200)),
                ('buyer_email', models.EmailField(max_length=75)),
                ('mobile_number', models.CharField(max_length=15)),
                ('seat_number', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('lunch_type', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('explara_barcode', models.CharField(max_length=100)),
                ('pesit_barcode', models.CharField(max_length=100)),
                ('had_lunch', models.BooleanField(default=False)),
                ('got_goodies_bag', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
