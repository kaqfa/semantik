# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='payment_for',
            field=models.CharField(default=b'p', max_length=1, choices=[(b's', b'Seminar'), (b'p', b'Pemakalah'), (b't', b'Makalah Tambahan')]),
        ),
        migrations.AlterField(
            model_name='fee',
            name='for_paper',
            field=models.ForeignKey(blank=True, to='papers.Paper', null=True),
        ),
    ]
