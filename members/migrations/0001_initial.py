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
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.CharField(default=b's', max_length=1, choices=[(b's', b'Terkirim'), (b'r', b'Terbaca'), (b'd', b'Terhapus')])),
                ('receiver', models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution', models.CharField(max_length=200, null=True, blank=True)),
                ('role', models.CharField(default=b'p', max_length=1, choices=[(b'a', b'Admin'), (b'p', b'Pemakalah'), (b's', b'Semiar'), (b'r', b'Reviewer')])),
                ('status', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'Aktif'), (b'b', b'Banned')])),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
