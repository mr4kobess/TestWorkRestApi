from rest_framework import serializers
from .models import Quiz, Question, Answer, ChoiceAnswer


class QuizListSerializer(serializers.ModelSerializer):
	"""
		Список опросов
	"""

	question = serializers.SlugRelatedField(slug_field='pk', read_only=True, many=True)

	class Meta:
		model = Quiz
		exclude = ('date_finish',)


class QuizDetailSerializer(serializers.ModelSerializer):
	""" Опрос """

	question = serializers.SlugRelatedField(slug_field='id', read_only=True, many=True, allow_empty=True)

	date_create = serializers.DateTimeField(read_only=True)

	class Meta:
		model = Quiz
		fields = '__all__'


class QuizCreateSerializer(serializers.ModelSerializer):
	""" Опрос """

	question = serializers.SlugRelatedField(slug_field='id', read_only=True, many=True)

	class Meta:
		model = Quiz
		fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
	"""
		Список вопросов
	"""

	choice_answer = serializers.SlugRelatedField(many=True, slug_field='pk', read_only=True)
	answer = serializers.SlugRelatedField(many=True, slug_field='text', read_only=True)

	class Meta:
		model = Question
		fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
	""" Детализация вопроса """

	choice_answer = serializers.SlugRelatedField(many=True, slug_field='pk', read_only=True)
	answer = serializers.SlugRelatedField(many=True, slug_field='pk', read_only=True, allow_null=False)

	class Meta:
		model = Question
		fields = ('text', 'type', 'quiz', 'choice_answer', 'answer')


class QuestionCreateSerializer(serializers.ModelSerializer):
	""" Создание вопроса """
	question = serializers.SlugRelatedField(slug_field='text', read_only=True)

	class Meta:
		model = Question
		fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'


class AnswerListSerializer(serializers.ModelSerializer):

	choice = serializers.SlugRelatedField(slug_field='text', read_only=True, allow_null=False, allow_empty=False)

	class Meta:
		model = Answer
		fields = '__all__'


class ChoiceAnswerDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = ChoiceAnswer
		fields = '__all__'