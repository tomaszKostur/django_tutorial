from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world from Polls index")

def detail(request, question_id):
    return HttpResponse("You're looking at question: {}".format(question_id))

def results(request, question_id):
    response = "You're looking at question: {}, results".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Voting for question: {}".format(question_id))
