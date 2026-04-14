from rest_framework import serializers    #serializer -module
from django.contrib.auth.models import User
from .models import Job, Application

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','password','email']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # 🔥 HASH HERE
        user.save()
        return user

class JobsSerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField()
    class Meta:
        model=Job
        fields="__all__"    # 'all' is special literal which takes all fields from model table

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields="__all__"