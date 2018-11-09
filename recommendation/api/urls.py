from django.urls import path
from api import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    # path('user/', views.user_geo),
]