# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_testorder_ordernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorder',
            name='orderNumber',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
