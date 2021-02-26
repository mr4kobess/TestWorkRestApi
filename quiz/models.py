from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
	""" Модель опроса """
	name = models.CharField(max_length=150, verbose_name='Название')
	date_start = models.DateTimeField(auto_now_add=True, null=True)
	date_finish = models.DateTimeField(null=True, blank=True)
	desc = models.TextField(null=True)

	class Meta:
		verbose_name = 'Опрос'
		verbose_name_plural = 'Опросы'

	def __str__(self):
		return self.name


class ChoiceAnswer(models.Model):
	text = models.CharField(max_length=200, verbose_name='Текст')
	question = models.ForeignKey('Question', related_name='choice_answer', on_delete=models.CASCADE)


class Question(models.Model):
	""" Модель вопроса """

	types = (('Text', 'text'), ('OneQ', 'one'),	('ManyQ', 'many'))

	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
	text = models.CharField(max_length=200, verbose_name='Вопрос')
	answer_options = models.TextField(verbose_name='Варианты', null=True, blank=True, default='')
	type = models.CharField(max_length=10, verbose_name='Тип вопроса', choices=types)

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		s = super(Question, self).save(force_insert=force_insert, force_update=force_update, using=using,
			update_fields=update_fields)
		if self.type in ['OneQ', 'ManyQ']:
			for t in self.answer_options.split(','):
				ChoiceAnswer.objects.create(question=self, text=t)
		return s

	def __str__(self):
		return self.text


class Answer(models.Model):

	user = models.ManyToManyField(User, related_name='answer', blank=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
	text = models.TextField(verbose_name='Текст', null=True, blank=True)
	choice = models.ForeignKey(ChoiceAnswer, verbose_name='Выбранный вариант', null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.text or self.choice.text

