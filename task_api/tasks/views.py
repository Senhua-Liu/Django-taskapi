from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django_q.tasks import async_task
from .tasks import process_task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        async_task(process_task, task.id)  # Lancer la tâche en arrière-plan
