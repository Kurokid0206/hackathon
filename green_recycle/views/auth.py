from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from hackathon.models import *
from .functions import check_request_type
from datetime import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .functions import AccountActivationTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        user = request.user
        return redirect("green_recycle:index")
    if request.method == "POST":
        username_or_email = request.POST.get("username_or_email")
        password = request.POST.get("password")

        try:
            username = User.objects.get(username=username_or_email).username
            user = authenticate(request, username=username, password=password)
        except:
            try:
                username = User.objects.get(email=username_or_email).username
                user = authenticate(request, username=username, password=password)
            except:
                return render(
                    request,
                    "green_recycle/login.html",
                    {"message": "Tài khoản chưa kích hoạt hoặc không tồn tại"},
                )

        if user is not None:
            if user.is_superuser:
                auth_login(request, user)
                try:
                    profile = UserProfile.objects.get(user = user)
                except:
                    new_profile = UserProfile(
                        user= user,
                        fullname= user.get_full_name(),
                        email= user.email,
                    )
                    new_profile.save()
                return redirect("green_recycle:index")
            if user.is_active:
                auth_login(request, user)
                return redirect("green_recycle:index")
        else:
            return render(
                request,
                "green_recycle/login.html",
                {"message": "Tài khoản chưa kích hoạt hoặc không tồn tại"},
            )
    else:
        return render(request, "green_recycle/login.html")


def register(request):
    is_login, flag_admin = check_request_type(request)

    if is_login == 1:
        return redirect("green_recycle:index")
    else:
        if request.method == "POST":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            date_of_birth = request.POST.get("dob")

            new_user = User()
            new_user.username = username
            new_user.last_name = lastname
            new_user.first_name = firstname
            new_user.email = email
            new_user.set_password(password1)
            new_user.date_joined = datetime.now()
            new_user.save()

            new_profile = UserProfile(
                user=new_user,
                fullname=firstname + " " + lastname,
                email=email,
                date_of_birth=date_of_birth,
            )
            new_profile.save()

            account_activation_token = AccountActivationTokenGenerator()
            current_site = get_current_site(request)
            subject = "Kích hoạt tài khoản cho hệ thống"
            message = render_to_string(
                "green_recycle/account_activation_email.html",
                {
                    "user": new_user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                    "token": account_activation_token.make_token(new_user),
                },
            )
            new_user.email_user(subject, message)

            context = {
                "new_profile": new_profile,
            }

            return redirect("green_recycle:account_activation_sent")
        else:
            return render(request, "green_recycle/register.html")


def account_activation_sent(request):
    return render(request, "green_recycle/verify-account.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    account_activation_token = AccountActivationTokenGenerator()
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return redirect("green_recycle:index")
    else:
        return render(
            request,
            "green_recycle/404.html",
            {"message": "Link kích hoạt không hợp lệ, vui lòng kiểm tra lại email."},
        )

def logout(request):
    try:
        auth_logout(request)
    except:
        pass
    return redirect("green_recycle:index")

