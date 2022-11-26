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
            date_of_birth = request.data.get("date_of_birth") #YYYY-MM-DD
            address = request.data.get("address")
            phone = request.data.get("phone")
            reference_id = request.data.get("reference_id")

            if password == re_password:
                user = User.objects.create_user(username=username, password=password)

                default_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "date_of_birth": date_of_birth,
                    "address": address,
                    "phone": phone,
                    "is_active": True,
                    "is_enable": True,
                }
                user_profile = UserProfile.objects.create(
                    user=user,
                    reference_id=reference_id,
                    **default_data,
                )
                user_profile.save()

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
                    profile = UserProfile.objects.get(user=user)
                    if user.is_superuser:
                        auth_login(request, user)
                        if not profile:
                            new_profile = UserProfile(
                                user=user,
                                fullname=user.get_full_name(),
                                email=user.email,
                            )
                            new_profile.save()

                        return JsonResponse({"status": "success", "message": "login successful"})
                    elif profile.is_active and profile.is_enable:
                        auth_login(request, user)
                        return JsonResponse({"status": "success", "message": "login successful"})
                    else:
                        return JsonResponse({"status": "fail", "message": "login failure, user is not active"})
            else:
                return JsonResponse({"status": "fail", "message": "login failure"})
        return JsonResponse({"status": "fail", "message": "login failure"})

    @action(detail=False, methods=['post'])
    def logout(self, request: Request):
        if request.method == 'POST':
            if request.user:
                auth_logout(request.user)
                return JsonResponse({"status": "success", "message": "logout successful"})
            return JsonResponse({"status": "fail", "message": "logout failure"})
        return JsonResponse({"status": "fail", "message": "logout failure"})

    @action(detail=False, methods=['post'])
    def activation(self, request: Request):
        pass

    @action(detail=False, methods=['post'])
    def upload_profile(self, request: Request):
        if request.method == 'POST':
            profile = UserProfile.objects.get(user=request.user)
            print("test", profile)
            first_name = request.data.get("first_name") if request.data.get("first_name") else profile.first_name
            last_name = request.data.get("last_name") if request.data.get("last_name") else profile.last_name
            email = request.data.get("email") if request.data.get("email") else profile.email
            date_of_birth = request.data.get("date_of_birth") if request.data.get("date_of_birth") else profile.date_of_birth #YYYY-MM-DD
            address = request.data.get("address") if request.data.get("address") else profile.address
            phone = request.data.get("phone") if request.data.get("phone") else profile.phone
            avatar = request.data.get("avatar") if request.data.get("avatar") else profile.avatar

            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            profile.date_of_birth = date_of_birth
            profile.address = address
            profile.phone = phone
            profile.avatar = avatar
            profile.save()

            return JsonResponse({"status": "success", "message": "profile saved"})
        return JsonResponse({"status": "fail", "message": "there're no summit"})
