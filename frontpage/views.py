from django.shortcuts import render
from django.template import RequestContext


def home(request):
    return render(request, 'frontpage/frontpage.html', {'title' : 'Home'})

def about(request):
    if request.user.is_authenticated:
        return render(request, 'frontpage/about.html', {'title' : 'About'})
    return render(request, 'frontpage/dick.html')
