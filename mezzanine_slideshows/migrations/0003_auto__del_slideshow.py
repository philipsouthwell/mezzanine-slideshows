# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Slideshow'
        db.delete_table('mezzanine_slideshows_slideshow')

        # Removing M2M table for field galleries on 'Slideshow'
        db.delete_table(db.shorten_name('mezzanine_slideshows_slideshow_galleries'))


    def backwards(self, orm):
        # Adding model 'Slideshow'
        db.create_table('mezzanine_slideshows_slideshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.RichTextPage'], unique=True)),
        ))
        db.send_create_signal('mezzanine_slideshows', ['Slideshow'])

        # Adding M2M table for field galleries on 'Slideshow'
        m2m_table_name = db.shorten_name('mezzanine_slideshows_slideshow_galleries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('slideshow', models.ForeignKey(orm['mezzanine_slideshows.slideshow'], null=False)),
            ('gallery', models.ForeignKey(orm['galleries.gallery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['slideshow_id', 'gallery_id'])


    models = {
        
    }

    complete_apps = ['mezzanine_slideshows']