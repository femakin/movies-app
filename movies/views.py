from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'movies': ['Gladiator', 'top gun', 'Ageshinkole']
    }

    # return HttpResponse('My Fav Movies')
    return render(request, 'movies/index.html',  context)


def about(request):
    # return HttpResponse('My Fav Movies')
    return render(request, 'movies/about.html', {})


#app/templates/app/index.html
#movies/templates/movies/index.html

