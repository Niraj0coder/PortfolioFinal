from .models import *
from rest_framework import serializers

class technologiesserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = technologies
        fields = "__all__"

class educationserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = education
        fields = "__all__"


class experienceserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = experiences
        fields = "__all__"

class projectserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = projects
        fields = "__all__"