from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from ..models.deck import Deck
from ...forms import AddDeckForm, UpdateDeckForm

def decks_index(request):
    """Index pages for decks, showing all decks"""
    decks = Deck.objects.all()
    template = loader.get_template('memecard_app/decks/index.html')
    context = {
        'decks': decks,
    }
    return HttpResponse(template.render(context, request))


def decks_detail(request, deck_id):
    """Detail page for a deck, showing all cards in the deck"""
    deck = get_object_or_404(Deck, pk=deck_id)
    cards = deck.card_set.all()
    deck.cards = []

    for card in cards:
        deck.cards.append(card)
        deck.cards[-1].faces = card.face_set.all()

    template = loader.get_template('memecard_app/decks/detail.html')
    context = {
        'deck': deck,
    }
    return HttpResponse(template.render(context, request))


def decks_create(request):
    """Present a form to create a new deck or parse the form data"""
    if request.method == 'POST':
        # Process the form data

        form = AddDeckForm(request.POST)

        if form.is_valid():
            new_deck = Deck()
            new_deck.name = form.cleaned_data['name']
            new_deck.public = form.cleaned_data['public']
            new_deck.strict_one_way = form.cleaned_data['strict_one_way']
            new_deck.card_type = form.cleaned_data['card_type']
            new_deck.save()

            return HttpResponseRedirect(reverse('decks_index'))
    else:
        # Present a blank form
        form = AddDeckForm()

    template = loader.get_template('memecard_app/decks/create.html')
    return HttpResponse(template.render({'form': form}, request))


def decks_update(request, deck_id):
    """Update a deck"""
    deck = get_object_or_404(Deck, pk=deck_id)

    if request.method == 'POST':
        # Process the form data

        form = UpdateDeckForm(request.POST)

        if form.is_valid():            
            deck.name = form.cleaned_data['name']
            deck.public = form.cleaned_data['public']
            deck.strict_one_way = form.cleaned_data['strict_one_way']            
            deck.save()

            return HttpResponseRedirect(reverse('decks_index'))
    else:
        # Present a blank form

        form = UpdateDeckForm(initial={
            'name': deck.name,
            'public': deck.public,
            'strict_one_way': deck.strict_one_way,
            'card_type': deck.card_type,
        })

    template = loader.get_template('memecard_app/decks/update.html')
    return HttpResponse(template.render({'form': form, 'deck': deck,}, request))


def decks_delete(request, deck_id):
    """Delete a deck"""
    pass