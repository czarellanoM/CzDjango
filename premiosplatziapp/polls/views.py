from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're seeing the results of question number %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
