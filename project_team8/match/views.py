from django.shortcuts import render, redirect
from .forms import CreateMatchForm
from .models import Match

def match_list(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'match/match_list.html', context)

def create_match(request):
    if request.method == 'POST':
        form = CreateMatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:match:match_list')
    else:
        form = CreateMatchForm()
    return render(request, 'match/create_match.html', {'form': form})

def join_match(request, match_id):
    match = Match.objects.get(pk=match_id)
    # 참가 처리 등을 수행
    # ...

    return redirect('main:match:match_list')