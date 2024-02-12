from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator

def home(request):
    quest = Question.objects.all().order_by('-id')
    paginator = Paginator(quest, 1)
    page_num = request.GET.get('page', 1)
    quest = paginator.page(page_num)
    return render(request, 'home.html', {'quest': quest})
