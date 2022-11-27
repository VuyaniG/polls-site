# Imports
from django.contrib import admin

from .models import Question, Choice



class ChoiceInline(admin.TabularInline):
    '''Choice model initialization in admin site in table layout'''
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    '''Question model initialization in admin site and layout declaration'''
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
