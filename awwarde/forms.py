from rest_framework import serializers

from .models import Profile, Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'link', 'rating')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', )