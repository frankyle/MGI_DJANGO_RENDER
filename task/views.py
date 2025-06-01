from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only tasks for the logged-in user are returned
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the user who creates the task
        serializer.save(user=self.request.user)
