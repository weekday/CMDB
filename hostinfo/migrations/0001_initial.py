# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf')),
                ('address', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf\xe5\x9c\xb0\xe5\x9d\x80')),
                ('contacts', models.CharField(max_length=64, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba')),
                ('conphone', models.CharField(max_length=16, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('remarks', models.CharField(max_length=1000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'db_table': 'Business',
                'verbose_name': '\u673a\u623f\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u623f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(null=True, verbose_name=b'IP')),
                ('root', models.CharField(max_length=64, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
                ('port', models.CharField(max_length=10, null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('cmd', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\x91\xbd\xe4\xbb\xa4')),
                ('user', models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\x80\x85')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4', null=True)),
            ],
            options={
                'db_table': 'History',
                'verbose_name': '\u5386\u53f2\u64cd\u4f5c',
                'verbose_name_plural': '\u5386\u53f2\u64cd\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=64, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\xbc\x96\xe5\x8f\xb7')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
                ('port', models.CharField(max_length=10, null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('username', models.CharField(max_length=64, null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7')),
                ('password', models.CharField(max_length=64, null=True, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe5\xaf\x86\xe7\xa0\x81')),
                ('osversion', models.CharField(max_length=64, null=True, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\x89\x88\xe6\x9c\xac')),
                ('memory', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('disk', models.CharField(max_length=64, null=True, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98')),
                ('sn', models.CharField(max_length=64, null=True, verbose_name=b'SN\xe5\x8f\xb7')),
                ('model_name', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('cpu', models.CharField(max_length=64, null=True, verbose_name=b'CPU')),
                ('remarks', models.CharField(max_length=1000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'db_table': 'Host',
                'verbose_name': '\u4e3b\u673a\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u4fe1\u606f',
            },
        ),
    ]
