from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from models import CardType


class AddUserForm(forms.Form):
    email = forms.EmailField(
        max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "onchange": "checkPassword()"}
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")
        if password != confirm:
            raise forms.ValidationError("Passwords do not match")


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})


class AddDeckForm(forms.Form):
    name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    public = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    strict_one_way = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    card_type = forms.ModelChoiceField(
        queryset=CardType.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-select"}),
    )


class UpdateDeckForm(forms.Form):
    name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    public = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    strict_one_way = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    card_type = forms.ModelChoiceField(
        queryset=CardType.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    strict_one_way.disabled = True
    card_type.disabled = True


class CardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        faces = kwargs.pop("faces")
        super().__init__(*args, **kwargs)
        for face in faces:
            self.fields[face.name] = forms.CharField(
                max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
            )
            self.fields[face.name + "_type"] = forms.CharField(widget=forms.HiddenInput)
            self.fields[face.name + "_type"].initial = face.face_type.id

    order = forms.IntegerField(
        min_value=0,
        max_value=1000,
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    public = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
