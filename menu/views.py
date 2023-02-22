from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def menu_item(request, slug):
    return render(request, 'home.html', {'slug': slug})
