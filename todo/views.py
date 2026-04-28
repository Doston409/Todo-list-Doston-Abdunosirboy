from rest_framework.generics import (
    ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .seralizers import TodoSerializer, TodoCreateSerializer, TodoUpdateSerializer



class TodoListAPIView(ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCreateAPIView(CreateAPIView):
    serializer_class = TodoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoUpdateSerializer
    permission_classes = [IsAuthenticated]


class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]