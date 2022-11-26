from rest_framework.viewsets import ModelViewSet

from hackathon.models import UserProfile
from hackathon.serializers.user import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
