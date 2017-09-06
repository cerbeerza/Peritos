from django.shortcuts import render
from django.contrib.auth.models import User

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

