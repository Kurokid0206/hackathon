from green_recycle.models import *
from django.shortcuts import render
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

def check_request_type(request):
    is_login = False
    flag_admin = False
    if request.user.is_authenticated:
        is_login = True
        user = request.user
        if user.is_superuser:
            flag_admin = True
        else:
            flag_admin = False

    return is_login, flag_admin

# def check_comment_table(request):
#     if request.user.is_authenticated:
#         if Rating.objects.filter(user=request.user).exists():
#             return 0
#     return 1


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp)
        )