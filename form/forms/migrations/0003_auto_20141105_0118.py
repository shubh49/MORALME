# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20141105_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='signupform',
        ),
    ]
