from django.shortcuts import render


def flite(requsest):
    return render(requsest, 'name1.html')


def name1(request):
    return render(request, 'flite test.html')


def spi(request):
    return render(request, 'Spitfair.html')


def fw(request):
    return render(request, 'fw-190.html')


def me(request):
    return render(request, 'me-262.html')


def Test(request):
    return render(request, 'Test.html')
