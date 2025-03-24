from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

    def create(self, validated_data):
        """Create and return a new User instance, given the validated data."""
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing User instance, given the validated data."""
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""
    
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users']

    def create(self, validated_data):
        """Create and return a new Task instance, given the validated data."""
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Task instance, given the validated data."""
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.completed_at = validated_data.get('completed_at', instance.completed_at)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance