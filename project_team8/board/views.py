from django.shortcuts import render, redirect
from .models import Post

def board_main(request):
    posts = Post.objects.all()
    return render(request, 'board/board_main.html', {'posts': posts})

def write(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()
        return redirect('board_main')
    return render(request, 'board/write.html', {'posts':posts})