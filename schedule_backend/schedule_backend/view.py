"""Some helper view"""
from django.shortcuts import redirect,render

def redirect_view(request):
    response = redirect('/api/')
    return response

def management(request):
    return render(request,'manage/index.html')