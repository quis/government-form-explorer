# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('attachment', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('ref', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=256)),
                ('size', models.IntegerField()),
                ('mime', models.CharField(max_length=128)),
                ('magic', models.CharField(max_length=256)),
                ('suffix', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=6)),
                ('count', models.IntegerField()),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Attachment')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('form', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('text', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('organisation', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('website', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('organisations', models.ManyToManyField(to='pages.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
        migrations.AddField(
            model_name='form',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Task'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Form'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
        migrations.AlterUniqueTogether(
            name='download',
            unique_together=set([('attachment', 'month')]),
        ),
    ]
