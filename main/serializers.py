from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Content
        fields = "__all__"




