from django.shortcuts import render
from django.views.generic import DetailView

from .models import Test


def register(request):
    return render(request, 'register.html')


def flite(request):
    return render(request, 'Corsair.html')


def home(request):
    aircrat = Test.objects.filter(categori="Самолет")
    kopter = Test.objects.filter(categori="Коптер")

    return render(request, 'Home.html', {'aircrat': aircrat, 'kopter': kopter})


def Spitfair(request):
    return render(request, 'Spitfair.html')


def fw(request):
    return render(request, 'fw-190.html')


def me(request):
    return render(request, 'me-262.html')


def kopter(request):
    return render(request, 'kopter.html')


def kon(request):
    return render(request, 'kon.html')


def kamikadze(request):
    return render(request, 'kamikadze.html')


def nachinka(request):
    return render(request, 'nachinka.html')




class DetalVievs(DetailView):
    model = Test
    template_name = 'Detal.html'
    context_object_name = 'object'
