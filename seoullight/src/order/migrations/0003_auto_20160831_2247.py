# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_testorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testorder',
            old_name='eMail',
            new_name='email',
        ),
    ]
