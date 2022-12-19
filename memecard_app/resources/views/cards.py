from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models.card import Card
from ..models.card_type_face_type import CardTypeFaceType
from ..models.face import Face
from ..models.deck import Deck
from ..models.card_user import CardUser
from ...forms import CardForm

def cards_index(request):
    return HttpResponseRedirect(reverse('index'))

def cards_detail(request, card_id):
    return HttpResponseRedirect(reverse('index'))

@login_required
def cards_create(request, deck_id):
    faces = CardTypeFaceType.getFaceFormDeck(deck_id)
    if request.method == 'POST':
        # Process the form data
        
        form = CardForm(request.POST, faces = faces)

        if form.is_valid():
            new_card = Card()
            new_card.creator = request.user
            new_card.deck = Deck.objects.get(pk=deck_id)
            new_card.order = form.cleaned_data['order']
            new_card.public = form.cleaned_data['public']
            new_card.nb_faces = len(faces)
            new_card.save()

            
            for face in faces:
                new_face = Face()
                new_face.card = new_card
                new_face.type_id = face.face_type_id
                new_face.content = form.cleaned_data[face.name]
                new_face.save()


            return HttpResponseRedirect(reverse('decks_detail', args=[deck_id]))
    else:
        # Present a blank form
        
        form = CardForm(faces = faces)

    template = loader.get_template('memecard_app/cards/create.html')
    return HttpResponse(template.render({'form': form, 'deck_id': deck_id}, request))


@login_required
def cards_update(request, card_id):
    '''update a card'''
    card = get_object_or_404(Card, pk=card_id)
    faces = CardTypeFaceType.getFaceFormDeck(card.deck.id)
    if request.method == 'POST':
        # Process the form data
        
        form = CardForm(request.POST, faces = faces)

        if form.is_valid():
            card.order = form.cleaned_data['order']
            card.public = form.cleaned_data['public']
            card.save()

            for face in faces:
                updated_face = Face.objects.get(card=card, type_id=face.face_type_id)
                updated_face.content = form.cleaned_data[face.name]
                updated_face.save()

            return HttpResponseRedirect(reverse('decks_detail', args=[card.deck.id]))
    else:
        # Present a prefilled form
        
        form = CardForm(faces = faces)

        form.fields['order'].initial = card.order
        form.fields['public'].initial = card.public

        for face in faces:
            old_face = Face.objects.get(card=card, type_id=face.face_type_id)
            form.fields[face.name].initial = old_face.content

    template = loader.get_template('memecard_app/cards/update.html')
    return HttpResponse(template.render({'form': form, 'card_id': card_id}, request))

@login_required
def cards_delete(request, card_id):
    '''delete a card'''
    card = get_object_or_404(Card, pk=card_id)

    if request.method == 'POST':
        card.delete()

    return HttpResponseRedirect(reverse('decks_detail', args=[card.deck.id]))

@login_required
def cards_learn(request, card_id):
    '''learn a card'''
    card = get_object_or_404(Card, pk=card_id)
    if request.method == 'POST':
        card_user = CardUser.objects.get(card=card, user=request.user)
        card_user.is_learned = True
        card_user.save()
        
    return HttpResponseRedirect(reverse('decks_learn', args=[card.deck.id]))
