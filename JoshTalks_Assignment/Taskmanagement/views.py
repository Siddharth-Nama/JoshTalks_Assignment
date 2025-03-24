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
    
class UserTasksView(generics.ListAPIView):
    """API View to get tasks assigned to a specific user."""
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        """Retrieve tasks assigned to the user specified by user_id."""
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)
 
class AssignTaskView(generics.UpdateAPIView):
    """API View to assign a task to one or more users."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        """Handle PATCH requests to assign users to a task."""
        try:
            task = self.get_object()  # This retrieves the task based on the provided ID
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        user_ids = request.data.get('user_ids', [])

        # Check if user_ids is provided and is a list
        if not isinstance(user_ids, list):
            return Response({"error": "user_ids must be a list."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate user IDs
        users = User.objects.filter(id__in=user_ids)
        if users.count() != len(user_ids):
            return Response({"error": "One or more user IDs are invalid."}, status=status.HTTP_400_BAD_REQUEST)

        # Assign the users to the task
        task.assigned_users.set(users)

        # Prepare the response data
        assigned_user_ids = task.assigned_users.values_list('id', flat=True)

        return Response({
            'message': 'Task assigned successfully',
            'assigned_user_ids': list(assigned_user_ids)
        }, status=status.HTTP_200_OK)
