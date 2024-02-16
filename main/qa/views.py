from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator

def home(request):
    if "qu" in request.GET:
        qu = request.GET['qu']
        quest = Question.objects.filter(title__icontains=qu).order_by('-id')
    else:
        quest = Question.objects.all().order_by('-id')
    paginator = Paginator(quest, 1)
    page_num = request.GET.get('page', 1)
    quest = paginator.page(page_num)
    return render(request, 'home.html', {'quest': quest})

def detail(request,id):
    quest = Question.objects.get(pk=id)
    return render(request,'detail.html',{'quest':quest})
    