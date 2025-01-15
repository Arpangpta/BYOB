from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def profile_list_view(request):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, "profiles/list.html", context)

# To print all the permissions that a model have: [in Shell]
# from django.contrib.auth.models import Permission
# qs = Permission.objects.all()
# for q in qs:
#     print(q)

# for obj in qs:
#    print(obj.content_type.app_label, obj.codename)

@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    user = request.user

    #print('user.has_perm("auth.view_user")', user.has_perm("auth.view_user"))
    #print('user.has_perm("visits.view_pagevisit")', user.has_perm("view_pagevisit"))

    # <app_label>.view_<model_name>
    # <app_label>.add_<model—name>
    # <app_label>.change_<model_name>
    # <app_label>.delete_<model_name>
    
    #profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "owner": is_me,
    }
    #return HttpResponse(f'Hello There {username}-{profile_user_obj.id}--{is_me}')
    return render(request, "profiles/detail.html", context)