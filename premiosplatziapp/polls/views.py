from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("You are on the main page of Platzi App awards")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're seeing the results of question number %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)