# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('author_title_date', models.CharField(serialize=False, max_length=500, primary_key=True)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=10000)),
                ('ip', models.CharField(null=True, max_length=20)),
                ('date', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PTT_User',
            fields=[
                ('user', models.CharField(serialize=False, max_length=50, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recommend_Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('score', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('friend', models.CharField(max_length=50)),
                ('relationship', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=50)),
                ('message', models.CharField(null=True, max_length=100)),
                ('status', models.CharField(max_length=1)),
                ('date', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ptt_user',
            name='relations',
            field=models.ManyToManyField(to='recommend.Relation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='reviews',
            field=models.ManyToManyField(to='recommend.Review'),
            preserve_default=True,
        ),
    ]
