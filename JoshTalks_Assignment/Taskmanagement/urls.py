from django.urls import path
from .views import *

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('tasks/create/', CreateTaskView.as_view(), name='create-task'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('tasks/', AllTasksView.as_view(), name='all-tasks'),
    path('tasks/<int:pk>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
]