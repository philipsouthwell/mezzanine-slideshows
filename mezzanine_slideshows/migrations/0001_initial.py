# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141227_0224'),
        ('galleries', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('slideshow_title', models.CharField(blank=True, help_text='A brief description of the slideshow', max_length=30)),
                ('slideshow_description', models.TextField(blank=True, help_text='A fuller description of the slideshow', max_length=100)),
                ('gallery', models.ForeignKey(to='galleries.Gallery')),
                ('page', models.OneToOneField(to='pages.RichTextPage')),
            ],
            options={
                'verbose_name_plural': 'Slideshows',
                'verbose_name': 'Slideshow',
            },
        ),
    ]
