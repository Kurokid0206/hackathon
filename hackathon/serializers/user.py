from rest_framework.fields import SerializerMethodField, IntegerField, CharField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from hackathon.models import UserProfile
from rest_framework.decorators import action


class UserProfileSerializer(ModelSerializer):
    point = IntegerField(read_only=True)
    username = CharField(required=True)
    password = CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"

    @action(detail=False, methods=["post"])
    def signup(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class UserSerializer(ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"
