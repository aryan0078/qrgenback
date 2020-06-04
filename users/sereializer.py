from rest_framework import serializers
from .models import Usersdata
class UsersdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usersdata
        fields="__all__"
