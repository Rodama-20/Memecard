from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models.card import Card
from ...forms import AddCardForm, UpdateCardForm

def cards_index(request):
    pass

def cards_detail(request, card_id):
    pass

@login_required
def cards_create(request):
    pass

@login_required
def cards_update(request, card_id):
    pass

@login_required
def cards_delete(request, card_id):
    pass