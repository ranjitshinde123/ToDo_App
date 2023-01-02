from .models import ToDo
from rest_framework import serializers
class ToDoserializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields=['id','title','discription','complete']

'''

'''