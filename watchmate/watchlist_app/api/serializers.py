from unicodedata import name
from wsgiref.validate import validator
from rest_framework import serializers
from watchlist_app.models import *


def name_length(value):
        if len(value)<4:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value    

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movie` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError('Name and Description should be different')
        else:
            return data



