from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>/', views.index, name='index'),
    # path('user/', views.user_geo),
]