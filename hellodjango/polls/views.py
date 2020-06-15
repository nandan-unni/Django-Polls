from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', { 'questions' : questions })

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)
