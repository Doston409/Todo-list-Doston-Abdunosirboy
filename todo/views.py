from rest_framework.viewsets import ModelViewSet
from .models import Todo, Test
from .seralizers import TodoSerializer, TestSerializer



class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
