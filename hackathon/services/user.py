from hackathon.models import User, UserProfile
from django.http import JsonResponse


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        user.save()

        reference_id = request.POST.get("reference_id")
        ref_user = User.objects.filter(username=reference_id)
        if ref_user.exists():
            user_profile = UserProfile.objects.create(
                user=user, reference_id=reference_id
            )
        else:
            JsonResponse({"status": "fail", "message": "Invalid reference id"})

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "fail"})
