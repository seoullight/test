# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eMail', models.EmailField(max_length=75, verbose_name='email')),
                ('state', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=100)),
                ('customerName', models.CharField(max_length=50)),
                ('baggageKind', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
