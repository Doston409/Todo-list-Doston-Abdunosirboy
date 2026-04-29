from rest_framework.serializers import ModelSerializer
from .models import Todo, Test

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'