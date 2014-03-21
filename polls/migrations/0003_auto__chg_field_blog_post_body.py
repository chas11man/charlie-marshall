# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Blog_Post.body'
        db.alter_column(u'polls_blog_post', 'body', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):

        # Changing field 'Blog_Post.body'
        db.alter_column(u'polls_blog_post', 'body', self.gf('django.db.models.fields.TextField')())

    models = {
        u'polls.blog_post': {
            'Meta': {'object_name': 'Blog_Post'},
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Question']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'polls.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'polls.resume': {
            'Meta': {'object_name': 'Resume'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'photos': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['polls']