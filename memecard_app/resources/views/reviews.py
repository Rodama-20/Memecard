from datetime import datetime
import json
from zoneinfo import ZoneInfo
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

from supermemo2 import SMTwo


from ..models.face_face_user import FaceFaceUser
from ..models.rev_log import RevLog


@login_required
def reviews(request, deck_id):
    """list all next_due form a deck for current user"""
    face_face = FaceFaceUser.objects.raw(
        """SELECT *
        FROM face_face_user
        JOIN faces ON face_face_user.face_one_id = faces.id
        JOIN cards ON faces.card_id = cards.id
        WHERE user_id = %s
        AND cards.deck_id = %s""",
        [request.user.id, deck_id],
    )

    template = loader.get_template("memecard_app/reviews/index.html")
    context = {
        "face_face": face_face,
    }
    return HttpResponse(template.render(context, request))


@login_required
@requires_csrf_token
def review(request):
    """review a card serie and update their next_due"""
    json_data = json.loads(request.body)
    for key in json_data:
        if json_data[key] is None:
            continue

        current = FaceFaceUser.objects.get(id=key)
        sm = SMTwo(
            current.easiness_factor, current.repetition, current.interval
        ).review(json_data[key])
        current.easiness_factor = sm.easiness
        current.repetition = sm.repetitions
        current.interval = sm.interval
        current.next_due = sm.review_date
        current.save()
        
        # Log the review
        revlog = RevLog()
        revlog.user = request.user
        revlog.card = current.face_one.card
        revlog.answer = json_data[key]
        revlog.interval = sm.interval
        revlog.easiness_factor = sm.easiness
        revlog.time = datetime.now(ZoneInfo("Europe/Zurich"))
        revlog.save()
        

    return HttpResponse("OK")
