# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('BirthdayCalendar_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('syw_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('BirthdayCalendar', ['User'])

        # Adding model 'UserFollowship'
        db.create_table('BirthdayCalendar_userfollowship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('followed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['BirthdayCalendar.User'], to_field='syw_id')),
            ('follower_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('follower_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('follower_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('birth_day', self.gf('django.db.models.fields.IntegerField')()),
            ('birth_month', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('BirthdayCalendar', ['UserFollowship'])

        # Adding unique constraint on 'UserFollowship', fields ['followed_by', 'follower_id']
        db.create_unique('BirthdayCalendar_userfollowship', ['followed_by_id', 'follower_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserFollowship', fields ['followed_by', 'follower_id']
        db.delete_unique('BirthdayCalendar_userfollowship', ['followed_by_id', 'follower_id'])

        # Deleting model 'User'
        db.delete_table('BirthdayCalendar_user')

        # Deleting model 'UserFollowship'
        db.delete_table('BirthdayCalendar_userfollowship')


    models = {
        'BirthdayCalendar.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'syw_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'BirthdayCalendar.userfollowship': {
            'Meta': {'unique_together': "(('followed_by', 'follower_id'),)", 'object_name': 'UserFollowship'},
            'birth_day': ('django.db.models.fields.IntegerField', [], {}),
            'birth_month': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'followed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['BirthdayCalendar.User']", 'to_field': "'syw_id'"}),
            'follower_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'follower_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'follower_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['BirthdayCalendar']