from . import views
from django.urls import path

urlpatterns = [
    path('rigist/', views.reg, name="regist"),
    path('h/', views.name1, name="Home"),
    path('c/', views.me, name="me"),
    path('Home/', views.flite, name="Karsar"),
    path('a/', views.fw, name="fw-190"),
    path('t/', views.Spitfair, name="Spitfair")
]