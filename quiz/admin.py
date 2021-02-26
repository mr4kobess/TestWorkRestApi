from django.contrib import admin
from .models import Quiz, Question, ChoiceAnswer, Answer
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe


admin.site.site_title = 'Опросник'
admin.site.site_header = 'Опросник'

admin.site.register(Answer)
# admin.site.register(QuestionText)


# admin.site.register(ChoiceAnswer)
# admin.site.register(QuestionMTM)


class ChoiceAnswerInline(admin.TabularInline):
	model = ChoiceAnswer
	fk_name = 'question'


class QuestionInline(admin.TabularInline):
	model = Question
	fk_name = 'quiz'


@admin.decorators.register(Quiz)
class Quiz(admin.ModelAdmin):
	inlines = [QuestionInline]
	fields = ['name', 'date_start', 'date_finish', 'desc', 'users']
	readonly_fields = ['date_start']


@admin.decorators.register(Question)
class QuestionMany(admin.ModelAdmin):
	inlines = [ChoiceAnswerInline]
