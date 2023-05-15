from django.shortcuts import render
from .models import Competition
from players.models import Player


def home(request):
    return render(request, 'main/base.html')

def competition_list(request):
    competitions = Competition.objects.all()
    
    context = {
        'competitions': competitions,
    }
    
    return render(request, 'competitions/competition_list.html', context)    

def search(request):
    query = request.GET.get('query', '')
    
    context = {
        'query': query,
    }
    
    return render(request, 'search/search.html', context)

def search_view(request):
    query = request.GET.get('query', '')
    results = []  

    context = {
        'results': results,
    }
    
    return render(request, 'search.html', context)

