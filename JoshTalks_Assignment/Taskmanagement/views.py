from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
class UserCreateView(generics.CreateAPIView):
    """API View to create a new user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """Handle POST requests for creating a user."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'mobile': user.mobile
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateTaskView(generics.CreateAPIView):
    """API View to create a new task."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        """Handle POST requests for creating a task."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()  # Save the task instance
            return Response({
                'id': task.id,  # Return the task ID
                'name': task.name,  # Assuming your Task model has a name field
                'description': task.description,  # Assuming your Task model has a description field
                # Add other fields as necessary
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllTasksView(generics.ListAPIView):
    """API View to retrieve all tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserListView(generics.ListAPIView):
    """API View to retrieve all users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        """Handle GET requests to retrieve all users."""
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    