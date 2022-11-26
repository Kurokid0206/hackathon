from rest_framework.viewsets import ModelViewSet

from hackathon.models import UserProfile, User
from django.http import JsonResponse
from rest_framework.request import Request

from hackathon.serializers.user import UserProfileSerializer
from rest_framework.decorators import action
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request: Request):
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
                    return JsonResponse({"status": "fail", "message": "Invalid reference id"})

                return JsonResponse({"status": "success"})

            return JsonResponse({"status": "fail"})

        return JsonResponse({"status": "fail"})

    @action(detail=False, methods=['post'])
    def login(self, request: Request):
        if request.method == "POST":
            username = request.data.get("username")
            password = request.data.get("password")
            username = User.objects.filter(username=username)
            username = username[0].username if username else None
            if username:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    profile = UserProfile.objects.filter(user=user)
                    if user.is_superuser:
                        auth_login(request, user)
                        if not profile:
                            new_profile = UserProfile(
                                user=user,
                                fullname=user.get_full_name(),
                                email=user.email,
                            )
                            new_profile.save()

                        data = {
                            "status": "success", 
                            "message": "Login successful"
                        }
                        return JsonResponse(data)
                    elif user.is_active and profile.is_active and profile.is_enable:
                        auth_login(request, user)
                        data = {
                            "status": "success", 
                            "message": "Login successful"
                        }
                        return JsonResponse(data)
                    else:
                        data = {
                            "status": "fail", 
                            "message": "Login failure, user is not active"
                        }
                        return JsonResponse(data)
            else:
                data = {
                    "status": "fail", 
                    "message": "Login failure"
                }
                return JsonResponse(data)
        data = {
            "status": "Fail",
            "message": "Login failure"
        }
        return JsonResponse(data)