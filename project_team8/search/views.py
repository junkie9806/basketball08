from django.shortcuts import render
from players.models import Player

def player_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        players = Player.objects.filter(playername__icontains=search_query)
        return render(request, 'search/player_search.html', {'players': players})
    return render(request, 'search/player_search.html')
