from django.contrib.auth.models import User
from hackathon.models import UserProfile
from django.dispatch import receiver
from django.db.models.signals import pre_save

# @receiver(pre_save, sender=UserProfile)
def seed_user(sender, instance, created, **kwargs):
    users = User.objects.all()
    print('hi')
    if users == []:
        User.objects.create_superuser(username='admin', password='1234')

    