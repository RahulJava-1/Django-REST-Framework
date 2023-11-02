from django.urls import path
from .views import *

#for registering viewset we use Router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')


urlpatterns = [
    path('',index,name='index'),
    path('post_todo/', post_todo, name='post_todo'),
    path('get_todo/',get_todo,name='get_todo'),
    path('patch_todo/',patch_todo,name='patch_todo'),


    path('todo/', TodoView.as_view()),
]

urlpatterns+=router.urls
