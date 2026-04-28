from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .seralizers import TodoSerializer



class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer