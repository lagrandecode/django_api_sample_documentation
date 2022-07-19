
from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
