from django.urls import path
from .views import TodoListAPIView,TodoCreateAPIView,TodoUpdateAPIView,TodoDestroyAPIView


urlpatterns = [
    path('todo-list/', TodoListAPIView.as_view()),
    path('todo-create/', TodoCreateAPIView.as_view()),
    path('todo-update/<int:pk>/', TodoUpdateAPIView.as_view()),
    path('todo-delete/<int:pk>/', TodoDestroyAPIView.as_view()),
]