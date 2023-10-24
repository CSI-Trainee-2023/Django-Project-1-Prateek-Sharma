from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('vote', views.vote, name = 'vote'),
    path('result', views.result, name = 'vote')
]