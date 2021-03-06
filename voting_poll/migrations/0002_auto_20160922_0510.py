# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting_poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'question', 'verbose_name_plural': 'questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=None, max_length=255, verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=255, verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='count',
            field=models.IntegerField(default=0, verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting_poll.Question', verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255, verbose_name='question'),
        ),
    ]
