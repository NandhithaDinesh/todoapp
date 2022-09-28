from rest_framework.serializers import ModelSerializer
from Todoapp.models import Todo
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todo
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Todo.objects.create(**validated_data,user=user)