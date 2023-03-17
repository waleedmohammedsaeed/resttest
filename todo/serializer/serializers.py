from rest_framework import  serializers
from todo.models import Actions


class ActionsSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Actions
        fields = '__all__'
