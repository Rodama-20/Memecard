"""Views for the memecard app

(c) 2023 He-Arc Cyrille Polier
"""

from django.http import HttpResponse
from django.template import loader

# import views from other files

from .resources.views.decks import *
from .resources.views.tags import *
from .resources.views.cards import *
from .resources.views.users import *
from .resources.views.reviews import *


# Create your views here.


def index(request):
    """Landing page for the website"""
    template = loader.get_template("memecard_app/index.html")
    return HttpResponse(template.render({}, request))


def about(request):
    """About page of the website"""
    template = loader.get_template("memecard_app/about.html")
    return HttpResponse(template.render({}, request))
