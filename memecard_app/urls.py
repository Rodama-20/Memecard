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
    
    # Card URLs
    path('cards/', views.cards_index, name='cards_index'),
    path('cards/<int:card_id>/', views.cards_detail, name='cards_detail'),
    path('cards/create/', views.cards_create, name='cards_create'),
    path('cards/<int:card_id>/update/', views.cards_update, name='cards_update'),
    path('cards/<int:card_id>/delete/', views.cards_delete, name='cards_delete'),

    # User URLs
    path('users/', views.users_index, name='users_index'),
    path('users/<int:user_id>/', views.users_detail, name='users_detail'),
    path('users/create/', views.users_create, name='users_create'),
    path('users/<int:user_id>/update/', views.users_update, name='users_update'),
    path('users/<int:user_id>/delete/', views.users_delete, name='users_delete'),
    path('accounts/profile/', views.users_profile, name='users_profile'),
]