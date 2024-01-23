
from django.urls import path, include

import watchlist_app
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, \
    WatchDetailAV, \
    StreamPlatformAV, \
    StreamPlatformDetailAV, \
    StreamPlatform, \
    ReviewList,\
    ReviewDetail, ReviewCreate

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_details'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]

