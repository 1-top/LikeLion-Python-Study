from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    """
    polls 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'polls/question_list.html', context)

def detail(request, question_id):
    """
    polls 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/question_detail.html', context)
