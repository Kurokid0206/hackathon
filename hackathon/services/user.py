from hackathon.models import User, UserProfile
from django.http import JsonResponse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        username = User.objects.filter(username=username)
        username = username[0].username if username else None
        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    auth_login(request, user)
                    profile = UserProfile.objects.filter(user=user)
                    if not profile:
                        new_profile = UserProfile(
                            user=user,
                            fullname=user.get_full_name(),
                            email=user.email,
                        )
                        new_profile.save()

                    data = {"status": "success", "message": "Login successful"}
                    return JsonResponse(data)
                if user.is_active:
                    auth_login(request, user)
                    data = {"status": "success", "message": "Login successful"}
                    return JsonResponse(data)
        else:
            data = {"status": "Fail", "message": "Login failure"}
            return JsonResponse(data)
    data = {"status": "Fail", "message": "Login failure"}
    return JsonResponse(data)
