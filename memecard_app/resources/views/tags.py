"""View module for handling requests about tags

(c) 2023 He-Arc Cyrille Polier
"""

from django.http import HttpResponse
from django.template import loader

from ..models.tag import Tag


def tags_index(request):
    """View function for the tags index page"""
    # Get all tags
    tags = Tag.objects.all()
    # Render the HTML template index.html with the data in the context variable
    template = loader.get_template("memecard_app/tags/index.html")
    context = {"tags": tags}
    return HttpResponse(template.render(context, request))


def tags_detail(request, tag_id):
    """View function for the tags detail page"""
    # Get all tags
    tag = Tag.objects.get(pk=tag_id)
    decks = tag.decks.all()
    # Render the HTML template index.html with the data in the context variable
    template = loader.get_template("memecard_app/tags/detail.html")
    context = {"tag": tag, "decks": decks}
    return HttpResponse(template.render(context, request))
