from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {'latest_question_list': latest_question_list}

    return HttpResponse(template.render(context, request))
    # or django shortcut for above is
    # return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    context = {'question': question}
    return render(request, 'detail.html', context)

def results(request, question_id):
    response = "You're looking at question: {}, results".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Voting for question: {}".format(question_id))
