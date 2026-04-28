from rest_framework.viewsets import ModelViewSet
from .models import User
from .seralizers import UserSerializer



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer