from django.urls import path
from api import views

urlpatterns = [
    path('', views.index),
    path('<int:page>/', views.index),
    # path('user/', views.user_geo),
]