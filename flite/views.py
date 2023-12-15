from django.shortcuts import render


def reg(request):
    return render(request, 'regist.html')


def name1(request):
    return render(request, 'flite test.html')


def flite(request):
    return render(request, 'name1.html')


def Spitfair(request):
    return render(request, 'Spitfair.html')


def fw(request):
    return render(request, 'fw-190.html')


def me(request):
    return render(request, 'me-262.html')


def Test(request):
    return render(request, 'Test.html')
