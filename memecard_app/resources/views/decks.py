from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models.deck import Deck
from ..models.card import Card
from ..models.face import Face
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

@login_required
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

@login_required
def decks_update(request, deck_id):
    """Update a deck"""
    deck = get_object_or_404(Deck, pk=deck_id)

    if request.method == 'POST':
        # Process the form data

        form = UpdateDeckForm(request.POST)

        if form.is_valid():            
            deck.name = form.cleaned_data['name']
            deck.public = form.cleaned_data['public']            
            deck.save()

            return HttpResponseRedirect(reverse('decks_index'))
    else:
        # Present a prefilled form

        form = UpdateDeckForm(initial={
            'name': deck.name,
            'public': deck.public,
            'strict_one_way': deck.strict_one_way,
            'card_type': deck.card_type,
        })

    template = loader.get_template('memecard_app/decks/update.html')
    return HttpResponse(template.render({'form': form, 'deck': deck,}, request))

@login_required
def decks_delete(request, deck_id):
    """Delete a deck"""
    pass

@login_required
def decks_subscribe(request, deck_id):
    """Subscribe to a deck"""

    deck = get_object_or_404(Deck, pk=deck_id)
    user = request.user
    if request.method == 'POST':
        # Process the form data
        user.decks.add(deck)

        return HttpResponseRedirect(reverse('decks_detail', args=(deck_id,)))
    else:
        return HttpResponseRedirect(reverse('decks_index'))

@login_required
def decks_unsubscribe(request, deck_id):
    """Subscribe to a deck"""

    deck = get_object_or_404(Deck, pk=deck_id)
    user = request.user
    if request.method == 'POST':
        # Process the form data
        user.decks.remove(deck)

        return HttpResponseRedirect(reverse('users_profile'))
    else:
        return HttpResponseRedirect(reverse('decks_index'))


@login_required
def decks_learn(request, deck_id):
    """Learn a deck"""
    params = {
        'deck_id': deck_id,
        'user_id': request.user.id,
    }
    cards = Card.objects.raw('''SELECT *
        FROM cards
        JOIN decks ON decks.id = cards.deck_id
        JOIN card_user ON card_user.card_id = cards.id
        WHERE decks.id = %(deck_id)s
        AND card_user.user_id = %(user_id)s
        AND card_user.is_learned = FALSE
        LIMIT 5'''
        , params)
    for card in cards:
        card.faces = card.face_set.all()

    template = loader.get_template('memecard_app/decks/learn.html')
    context = {
        'cards': cards,
    }
    return HttpResponse(template.render(context, request))

@login_required
def decks_review(request, deck_id):
    """Review a deck"""
    params = {
        'deck_id': deck_id,
        'user_id': request.user.id,
    }
    faces1 = Face.objects.raw('''SELECT *
        FROM faces
        JOIN face_face_user ON face_face_user.face_one_id = faces.id
        JOIN cards ON cards.id = faces.card_id
        JOIN decks ON decks.id = cards.deck_id
        WHERE face_face_user.user_id = %(user_id)s
        AND decks.id = %(deck_id)s
        AND face_face_user.next_due <= NOW()
        '''
        , params)
    faces2 = Face.objects.raw('''SELECT *
        FROM faces
        JOIN face_face_user ON face_face_user.face_two_id = faces.id
        JOIN cards ON cards.id = faces.card_id
        JOIN decks ON decks.id = cards.deck_id
        WHERE face_face_user.user_id = %(user_id)s
        AND decks.id = %(deck_id)s
        AND face_face_user.next_due <= NOW()
        '''
        , params)

    faces = map(lambda x, y: (x, y), faces1, faces2)
    template = loader.get_template('memecard_app/decks/review.html')
    context = {
        'faces': faces,
    }
    return HttpResponse(template.render(context, request))