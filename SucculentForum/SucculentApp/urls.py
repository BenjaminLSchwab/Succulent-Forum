from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Register', views.register, name='register'),
    path('<int:topic_id>/Topic/NewThread/', views.newThread, name='newThread')
]
