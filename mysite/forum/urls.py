from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:topic_name>/', views.topic_view, name='topic'),
]
