from django import forms

from .models import CardType

class AddUserForm(forms.Form):
    email = forms.EmailField(max_length=50)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget = forms.PasswordInput())    
    confirm = forms.CharField(widget = forms.PasswordInput())

    def is_valid(self) -> bool:
        password_check = self.cleaned_data['password'] == self.cleaned_data['confirm']
        return super().is_valid() and password_check


class AddDeckForm(forms.Form):
    name = forms.CharField(max_length=30 )
    public = forms.BooleanField(required=False)
    strict_one_way = forms.BooleanField(required=False)
    card_type = forms.ModelChoiceField(queryset=CardType.objects.all())

class UpdateDeckForm(forms.Form):
    name = forms.CharField(max_length=30 )
    public = forms.BooleanField(required=False)
    strict_one_way = forms.BooleanField(required=False)
    card_type = forms.ModelChoiceField(queryset=CardType.objects.all(), required=False)
    strict_one_way.disabled = True
    card_type.disabled = True


class AddCardForm(forms.Form):
    pass

class UpdateCardForm(forms.Form):
    pass

