# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrapup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='prettyDate',
            field=models.CharField(default='Now', max_length=200),
            preserve_default=False,
        ),
    ]
