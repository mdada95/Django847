# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Question 

# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'owner', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
	'classes': ['collapse']}),
    ]
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
	if db_field.name == "questions": 
		kwargs["queryset"] = Question.objects.filter(owner=request.user)
	return super(QuestionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
