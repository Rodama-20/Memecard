from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from resources.models.user import User
from forms import AddUserForm


def users_index(request):
    pass


def users_detail(request, user_id):
    pass


def users_create(request):
    if request.method == "POST":
        # Process the form data

        form = AddUserForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.username = form.cleaned_data["username"]
            new_user.email = form.cleaned_data["email"]
            new_user.password = form.cleaned_data["password"]
            new_user.save()

            return HttpResponseRedirect(reverse("index"))
    else:
        # Present a blank form
        form = AddUserForm()
    template = loader.get_template("memecard_app/users/create.html")
    return HttpResponse(template.render({"form": form}, request))


def users_update(request, user_id):
    pass


def users_delete(request, user_id):
    pass


@login_required
def users_profile(request):
    decks = request.user.decks.all()
    template = loader.get_template("memecard_app/users/profile.html")
    return HttpResponse(template.render({"decks": decks}, request))
