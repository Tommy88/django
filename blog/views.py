from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog_list(request):
    n = 'Hello World'
    return render(request, 'blog/index.html', context={'phrase': n})
