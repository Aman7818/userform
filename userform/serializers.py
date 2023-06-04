from rest_framework import serializers
from userform.models import UserForm

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = '__all__'
