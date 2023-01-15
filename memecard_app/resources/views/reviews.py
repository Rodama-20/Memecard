from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

from supermemo2 import SMTwo


from ..models.face_face_user import FaceFaceUser


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

    for face in face_face:
        print(face)

    template = loader.get_template("memecard_app/reviews/index.html")
    context = {
        "face_face": face_face,
    }
    return HttpResponse(template.render(context, request))


@login_required
@requires_csrf_token
def review(request, face_face_user_id):
    """review a card and update the next_due"""
    if request.method == "POST":
        # Process the form data
        review = get_object_or_404(FaceFaceUser, pk=face_face_user_id)

        evaluation = int(request.POST["evaluation"])
        sm = SMTwo(review.easiness_factor, review.repetition, review.interval).review(
            evaluation
        )
        review.easiness_factor = sm.easiness
        review.repetition = sm.repetitions
        review.interval = sm.interval
        review.next_due = sm.review_date
        review.save()

        deck_id = review.face_one.card.deck.id

        return HttpResponseRedirect(reverse("decks_review", args=(deck_id,)))

    return HttpResponseRedirect(reverse("index"))
