# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slideshow'
        db.create_table('mezzanine_slideshows_slideshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['pages.RichTextPage'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
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


    def backwards(self, orm):
        # Deleting model 'Slideshow'
        db.delete_table('mezzanine_slideshows_slideshow')

        # Removing M2M table for field galleries on 'Slideshow'
        db.delete_table(db.shorten_name('mezzanine_slideshows_slideshow_galleries'))


    models = {
        'galleries.gallery': {
            'Meta': {'_ormbases': ['pages.Page'], 'object_name': 'Gallery', 'ordering': "('_order',)"},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['pages.Page']"}),
            'zip_import': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '100'})
        },
        'mezzanine_slideshows.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'galleries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['galleries.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['pages.RichTextPage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "('titles',)"},
            '_meta_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '500', 'null': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'blank': 'True', 'max_length': '100', 'default': '(1, 2, 3)', 'null': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '500'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2000', 'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'pages.richtextpage': {
            'Meta': {'_ormbases': ['pages.Page'], 'object_name': 'RichTextPage', 'ordering': "('_order',)"},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['pages.Page']"})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'", 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['mezzanine_slideshows']