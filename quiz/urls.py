from django.urls import path, include
from .views import QuizListView, QuizDetailView, QuizCreateView, QuizUpdateView, QuizDeleteView,  \
	QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView,\
	QuestionDeleteView, AnswerCreateView, AnswersUserListView, ChoiceAnswerDetailView

urlpatterns = [
	path('quiz/', QuizListView.as_view()),
	path('quiz/get/<int:pk>/', QuizDetailView.as_view()),
	path('quiz/create/', QuizCreateView.as_view()),
	path('quiz/update/<int:pk>/', QuizUpdateView.as_view()),
	path('quiz/delete/<int:pk>/', QuizDeleteView.as_view()),

	path('question/', QuestionListView.as_view()),
	path('question/get/<int:pk>/', QuestionDetailView.as_view()),
	path('question/create/', QuestionCreateView.as_view()),
	path('question/update/<int:pk>/', QuestionUpdateView.as_view()),
	path('question/delete/<int:pk>/', QuestionDeleteView.as_view()),

	path('answer/create/', AnswerCreateView.as_view()),
	path('answer/get/<int:pk>/', AnswersUserListView.as_view()),

	path('choiceanswer/get/<int:pk>/', ChoiceAnswerDetailView.as_view()),
]
