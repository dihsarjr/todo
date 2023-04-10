from django.urls import path
from todo_api.views import TodoList,AddTodo

urlpatterns = [
    path('list/',TodoList.as_view()),
    path('',AddTodo.as_view()) 
]