# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eMail', models.EmailField(max_length=75, verbose_name='email')),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('nation', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(to='order.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
