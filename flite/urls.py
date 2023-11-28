from . import views
from django.urls import path

urlpatterns = [
    path('', views.name1, name="cf"),
    path('h/', views.flite, name="in"),
    path('c/', views.me, name="cl"),
    path('a/', views.fw, name="vf"),
    path('t/', views.spi, name="vp")]
