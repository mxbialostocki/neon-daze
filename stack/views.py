from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('stack/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'stack/details.html', {'question': question})