from hackathon.models import User, UserProfile
from django.http import JsonResponse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        phone = request.POST['phone']

        if password == re_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        
            reference_id = request.POST.get("reference_id")
            ref_user = User.objects.filter(username=reference_id)
            if ref_user.exists():
                default_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'date_of_birth': date_of_birth,
                    'address': address,
                    'phone': phone,
                }
                user_profile = UserProfile.objects.create(
                    user=user, 
                    reference_id=reference_id, 
                    # **default_data,
                )
            else:
                JsonResponse({"status": "fail", "message": "Invalid reference id"})

            return JsonResponse({"status": "success"})

        return JsonResponse({"status": "fail"})

    return JsonResponse({"status": "fail"})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
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
                            user= user,
                            fullname= user.get_full_name(),
                            email= user.email,
                        )
                        new_profile.save()
                    
                    data = {
                        "status": "success", 
                        "message": "Login successful"
                    }
                    return JsonResponse(data)
                if user.is_active:
                    auth_login(request, user)
                    data = {
                        "status": "success", 
                        "message": "Login successful"
                    }
                    return JsonResponse(data)
        else:
            data = {
                "status": "Fail", 
                "message": "Login failure"
            }
            return JsonResponse(data)
    data = {
        "status": "Fail", 
        "message": "Login failure"
    }
    return JsonResponse(data)
