from django.shortcuts import render
# from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    
    # context = {
    #     'name' : 'Aqeel',
    #     'age' : 25,
    #     'nationality' : 'Pakistani'
    # }
    # return HttpResponse("<h1> Welcome to MyApp <h1/>")
    # return render(request, 'index.html', {'name' : username})
    # return render(request, 'index.html', context)
    return render(request, 'index.html')

    
def counter(request):
    text = request.POST['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'word_count' : word_count})


def index2(request):
    return render(request, 'index2.html')
