from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quiz, Question, ChoiceAnswer, Answer
from .serializers import QuizListSerializer, QuizDetailSerializer, QuizCreateSerializer, QuestionListSerializer, \
	QuestionDetailSerializer, QuestionCreateSerializer, AnswerCreateSerializer, AnswerListSerializer, \
	ChoiceAnswerDetailSerializer


class QuizListView(APIView):
	""" Вывод списка опросов """

	# authentication_classes = [TokenAuthentication]

	def get(self, request):
		quiz = Quiz.objects.filter(date_finish=None)
		serializer = QuizListSerializer(quiz, many=True)
		return Response(serializer.data)


class QuizDetailView(APIView):
	""" Вывод опросоа """

	def get(self, request, pk):
		quiz = get_object_or_404(Quiz, id=pk)
		serializer = QuizDetailSerializer(quiz)
		return Response(serializer.data)


class QuizCreateView(APIView):
	def post(self, request):
		serializer = QuizCreateSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class QuizUpdateView(APIView):

	def post(self, request, pk):
		quiz = get_object_or_404(Quiz, id=pk)
		serializer = QuizDetailSerializer(data=request.data, instance=quiz)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class QuizDeleteView(APIView):

	def post(self, request, pk):
		quiz = get_object_or_404(Quiz, id=pk)
		quiz.delete()
		return Response(status=204)


# -----------------------------------------------< Question >------------------------------------------

class QuestionListView(APIView):
	""" Вывод списка вопросов """

	# authentication_classes = [TokenAuthentication]

	def get(self, request):
		question = Question.objects.filter()
		serializer = QuestionListSerializer(question, many=True)
		return Response(serializer.data)


class QuestionDetailView(APIView):
	""" Вывод вопросоа """

	def get(self, request, pk):
		question = get_object_or_404(Question, id=pk)
		serializer = QuestionDetailSerializer(question)
		return Response(serializer.data)


class QuestionCreateView(APIView):
	def post(self, request):
		serializer = QuestionCreateSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class QuestionUpdateView(APIView):

	def post(self, request, pk):
		question = get_object_or_404(Question, id=pk)
		serializer = QuestionDetailSerializer(data=request.data, instance=question)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class QuestionDeleteView(APIView):

	def post(self, request, pk):
		question = get_object_or_404(Question, id=pk)
		question.delete()
		return Response(status=204)


class AnswerCreateView(APIView):
	def post(self, request):
		serializer = AnswerCreateSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class AnswersUserListView(APIView):
	""" Вывод списка опросов """

	def get(self, request, pk):
		answers = Answer.objects.filter(user=pk)
		quiz_pks = [i.question.quiz.pk for i in answers]
		quiz = Quiz.objects.filter(pk__in=quiz_pks)

		serializer_quiz = QuizListSerializer(quiz, many=True)
		serializer_answer = AnswerListSerializer(answers, many=True)
		return Response({'answers': serializer_answer.data,
						 'quiz': serializer_quiz.data})


class ChoiceAnswerDetailView(APIView):

	def get(self, request, pk):
		choice_answer = get_object_or_404(ChoiceAnswer, id=pk)
		serializer = ChoiceAnswerDetailSerializer(choice_answer)
		return Response(serializer.data)
