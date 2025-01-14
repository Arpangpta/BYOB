from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def profile_list_view(request, username=None, *args, **kwargs):
    # context = {
    #     "object_list": User.objects.filter(is_active=True)
    # }
    user = request.user
    #profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    return HttpResponse(f'Hello There {username}-{profile_user_obj.id}')#render(request, "profiles/list.html", context)