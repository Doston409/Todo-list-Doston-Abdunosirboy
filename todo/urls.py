from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TestViewSet

r = DefaultRouter()
r.register("todo", TodoViewSet)
r.register("test", TestViewSet)

urlpatterns = [
    path('', include(r.urls)),
]