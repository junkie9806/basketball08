from django.shortcuts import render

# Create your views here.
def search_main(request):
    return render(request, 'search/search_main.html')