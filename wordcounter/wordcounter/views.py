from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def count(request):
    t=request.GET['fulltext']
    l=[i for i in t.split()]

    return render(request,'count.html',{'n':len(l)})


def about(request):
    return render(request,'about.html')
