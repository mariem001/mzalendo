# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('core_person', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('date_of_death', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200, db_index=True)),
            ('middle_names', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_birth', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Person'])

        # Adding model 'Organisation'
        db.create_table('core_organisation', (
            ('organisation_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('started', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200, db_index=True)),
            ('ended', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Organisation'])

        # Adding model 'Place'
        db.create_table('core_place', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Organisation'], null=True)),
            ('shape_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('place_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['Place'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('core_person')

        # Deleting model 'Organisation'
        db.delete_table('core_organisation')

        # Deleting model 'Place'
        db.delete_table('core_place')
    
    
    models = {
        'core.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'ended': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organisation_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'started': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10'})
        },
        'core.person': {
            'Meta': {'object_name': 'Person'},
            'date_of_birth': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10'}),
            'date_of_death': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'core.place': {
            'Meta': {'object_name': 'Place'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Organisation']", 'null': 'True'}),
            'place_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['core']