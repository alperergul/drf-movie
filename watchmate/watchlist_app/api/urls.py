
from django.urls import path, include

import watchlist_app
from watchlist_app.api.views import movie_list, movie_details

urlpatterns = [
    path('list', movie_list, name='movie_list'),
    path('<int:pk>', movie_details, name='movie_details'),

]

