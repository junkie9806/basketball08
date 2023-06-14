from django.shortcuts import render, redirect
from .models import Post

def board_main(request):
    posts = Post.objects.all()
    return render(request, 'board/board_main.html', {'posts': posts})

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        creator = request.user
        post = Post.objects.create(title=title, content=content, creator=creator)
        
        return redirect('main:board:board_main')
    return render(request, 'board/write.html')