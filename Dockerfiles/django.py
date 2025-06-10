from django.db import models
from django.urls import path
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Model
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']

# ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Simple API view for demonstration
@api_view(['GET'])
def task_count(request):
    count = Task.objects.count()
    return Response({'total_tasks': count})

# URL patterns
urlpatterns = [
    path('api/tasks/count/', task_count, name='task-count'),
]
