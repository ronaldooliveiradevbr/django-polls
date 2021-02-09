from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    return render(request, 'core/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("ok")


def vote(request, question_id):
    return HttpResponse("ok")
