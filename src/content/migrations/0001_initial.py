# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('display_initials', models.CharField(max_length=3)),
                ('image', models.ImageField(null=True, upload_to='categories/', blank=True)),
                ('is_active', models.BooleanField(verbose_name='Active:')),
            ],
        ),
    ]
