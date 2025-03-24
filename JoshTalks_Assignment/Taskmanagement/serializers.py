from rest_framework import serializers
from .models import *

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

