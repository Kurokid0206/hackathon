from rest_framework.viewsets import ModelViewSet

from hackathon.models import UserProfile, User
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response

from hackathon.serializers.user import UserProfileSerializer
from rest_framework.decorators import action

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request: Request):
        print(request.data)
        if request.method == "POST":
            username = request.data.get("username")
            password = request.data.get("password")
            re_password = request.data.get("re_password")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            email = request.data.get("email")
            date_of_birth = request.data.get("date_of_birth")
            address = request.data.get("address")
            phone = request.data.get("phone")

            if password == re_password:
                user = User.objects.create_user(username=username, password=password)

                reference_id = request.POST.get("reference_id")
                ref_user = User.objects.filter(username=reference_id)
                if ref_user.exists():
                    default_data = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "date_of_birth": date_of_birth,
                        "address": address,
                        "phone": phone,
                    }
                    user_profile = UserProfile.objects.create(
                        user=user,
                        reference_id=reference_id,
                        default_data=default_data,
                    )
                else:
                    return Response({"status": "fail", "message": "Invalid reference id"})

                return Response({"status": "success"})

            return Response({"status": "fail"})

        return Response({"status": "fail"})
