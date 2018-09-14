from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    context = {'questions': Question.objects.all()}
    return render(request, 'core/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/detail.html', {'question': question})
