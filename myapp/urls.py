from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('post_todo/', post_todo, name='post_todo'),
    path('get_todo/',get_todo,name='get_todo'),
    path('patch_todo/',patch_todo,name='patch_todo'),


    path('todo/', TodoView.as_view()),
]
