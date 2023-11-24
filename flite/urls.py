from . import views
from django.urls import path

urlpatterns = [
    path('', views.name, name="cf"),
    path('h/', views.flite, name="main"),
    path('c/', views.me, name="cl"),
    path('a/', views.fw, name="vf"),
    path('t/', views.spi, name="vp")]
