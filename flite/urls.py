from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name="register"),
    path('', views.home, name="Home"),
    path('me/', views.me, name="me"),
    path('Corsair/', views.flite, name="Corsair"),
    path('fw/', views.fw, name="fw"),
    path('Spitfair/', views.Spitfair, name="Spitfair"),
    path('kopter/', views.kopter, name="kopter"),
    path('kon/', views.kon, name="kon"),
    path('kamikadze/', views.kamikadze, name="kamikadze"),
    path('nachinka/', views.nachinka, name="nachinka"),
    path('nob/', views.nob, name="nob"),
    path('detal/<int:pk>/', views.DetalVievs.as_view(), name='detal'),


]
