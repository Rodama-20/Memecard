from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from ..models.user import User

def users_index(request):
    pass

def users_detail(request, user_id):
    pass

def users_create(request):
    pass

def users_update(request, user_id):
    pass

def users_delete(request, user_id):
    pass

def users_profile(request):
    pass
