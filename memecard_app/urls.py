from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # Deck URLs
    path('decks/', views.decks_index, name='decks_index'),
    path('decks/<int:deck_id>/', views.decks_detail, name='decks_detail'),
    path('decks/create/', views.decks_create, name='decks_create'),
    path('decks/<int:deck_id>/update/', views.decks_update, name='decks_update'),
    path('decks/<int:deck_id>/delete/', views.decks_delete, name='decks_delete'),
    path('decks/<int:deck_id>/subscribe/', views.decks_subscribe, name='decks_subscribe'),
    path('decks/<int:deck_id>/unsubscribe/', views.decks_unsubscribe, name='decks_unsubscribe'),
    path('decks/<int:deck_id>/learn/', views.decks_learn, name='decks_learn'),
    path('decks/<int:deck_id>/review/', views.decks_review, name='decks_review'),
    
    # Card URLs
    path('cards/', views.cards_index, name='cards_index'),
    path('cards/<int:card_id>/', views.cards_detail, name='cards_detail'),
    path('cards/create/<int:deck_id>/', views.cards_create, name='cards_create'),
    path('cards/<int:card_id>/update/', views.cards_update, name='cards_update'),
    path('cards/<int:card_id>/delete/', views.cards_delete, name='cards_delete'),
    path('cards/<int:card_id>/learn/', views.cards_learn, name='cards_learn'),

    # User URLs
    path('users/', views.users_index, name='users_index'),
    path('users/<int:user_id>/', views.users_detail, name='users_detail'),
    path('users/create/', views.users_create, name='users_create'),
    path('users/<int:user_id>/update/', views.users_update, name='users_update'),
    path('users/<int:user_id>/delete/', views.users_delete, name='users_delete'),
    path('users/profile/', views.users_profile, name='users_profile'),

    # Review URLs
    path('review/<int:face_face_user_id>/', views.review, name='review'),
    path('reviews/<int:deck_id>', views.reviews, name='reviews_index'),
]