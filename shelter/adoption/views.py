from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Dog


doggos = [
    {'id': 1, 'name': 'Cody', 'breed': 'Cockapoo', 'owner': 'Yvonne'},
    {'id': 2, 'name': 'Luffy', 'breed': 'Shiba', 'owner': 'Kieran'},
    {'id': 3, 'name': 'Yami', 'breed': 'Shiba', 'owner': 'Trevor'}
]
# Create your views here.


def home(request):
    return render(request, 'adoption/home.html')


def about(request):
    return render(request, 'adoption/about.html')


def dogs(request):
    data = {'doggos': Dog.objects.all()}
    return render(request, 'adoption/dogs.html', data)


def show(request, id):
    # dog = list(filter(lambda doggo: doggo['id'] == id, doggos))
    dog = get_object_or_404(Dog, pk=id)
    data = {'dog': dog}
    return render(request, 'adoption/show.html', data)


def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)


def server_error_500(request):
    return render(request, '500.html')
