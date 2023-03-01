from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class TypeOfUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOfUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    type_of_user = TypeOfUserSerializer(read_only=True)
    Type_of_user_id = serializers.PrimaryKeyRelatedField(
        queryset=TypeOfUser.objects.all(),
        source="type_of_user"
    )
    
    class Meta:
        model = User
        fields = '__all__'