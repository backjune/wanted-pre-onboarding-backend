from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError('Email must contain the @ symbol.')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        return value
