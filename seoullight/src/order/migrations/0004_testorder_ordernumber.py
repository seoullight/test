# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20160831_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='testorder',
            name='orderNumber',
            field=models.CharField(default=datetime.datetime(2016, 9, 2, 12, 50, 13, 331000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
