# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('the_file', models.FileField(upload_to=b'')),
                ('upload_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('abstract', models.TextField()),
                ('keywords', models.CharField(max_length=200)),
                ('status', models.CharField(default=b's', max_length=1, choices=[(b's', b'Submitted'), (b'p', b'Pending Review'), (b'a', b'Accepted')])),
                ('category', models.ForeignKey(to='papers.Category')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nil_a', models.IntegerField(default=0, null=True, blank=True)),
                ('nil_b', models.IntegerField(default=0, null=True, blank=True)),
                ('nil_c', models.IntegerField(default=0, null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('for_paper', models.ForeignKey(to='papers.Paper')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='filehistory',
            name='for_paper',
            field=models.ForeignKey(to='papers.Paper'),
        ),
    ]
