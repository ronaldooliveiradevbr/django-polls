from django.shortcuts import render


def index(request):
    latest_question_list = [
        {'id': 1, 'text': 'What is your favorite color?'},
        {'id': 2, 'text': 'Who is going to win the election?'},
        {'id': 3, 'text': 'Do you believe in aliens?'},
    ]

    return render(request, 'core/index.html', {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    question = {
        'id': 1,
        'text': 'What is your favorite color?',
        'choices': [
            {'id': 1, 'text': 'Red'},
            {'id': 2, 'text': 'Blue'},
            {'id': 3, 'text': 'None'},
        ],
    }
    return render(request, 'core/detail.html', {'question': question})
