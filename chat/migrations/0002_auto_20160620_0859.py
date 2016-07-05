# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='chat_user',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Color'),
        ),
    ]