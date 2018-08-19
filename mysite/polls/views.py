from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}

    return HttpResponse(template.render(context, request))
    # or django shortcut for above is
    # return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at question: {}, results".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Voting for question: {}".format(question_id))
