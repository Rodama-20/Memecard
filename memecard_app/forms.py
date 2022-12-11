from django import forms

from .models import CardType


class AddDeckForm(forms.Form):
    name = forms.CharField(max_length=30 )
    public = forms.BooleanField(required=False)
    strict_one_way = forms.BooleanField(required=False)
    card_type = forms.ModelChoiceField(queryset=CardType.objects.all())

class UpdateDeckForm(forms.Form):
    name = forms.CharField(max_length=30 )
    public = forms.BooleanField(required=False)
    strict_one_way = forms.BooleanField(required=False)
    card_type = forms.ModelChoiceField(queryset=CardType.objects.all())
    strict_one_way.disabled = True
    card_type.disabled = True


class AddCardForm(forms.Form):
    pass

class UpdateCardForm(forms.Form):
    pass

