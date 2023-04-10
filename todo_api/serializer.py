from rest_framework import serializers
from todo_api.models import TodoModel


class TodoModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
