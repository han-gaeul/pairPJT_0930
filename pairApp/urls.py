from django.urls import path
from . import views


app_name = 'pairApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('new/', views.new, name='new')
]