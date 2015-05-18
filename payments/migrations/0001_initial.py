# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=1, choices=[(b'w', b'Wait'), (b'b', b'Billed'), (b'P', b'Paid')])),
                ('for_paper', models.ForeignKey(to='papers.Paper', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('the_file', models.FileField(upload_to=b'')),
                ('status', models.CharField(max_length=1, choices=[(b'p', b'Pending'), (b'c', b'Confirmed')])),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
