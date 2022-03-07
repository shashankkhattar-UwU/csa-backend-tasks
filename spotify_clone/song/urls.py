from django.urls import path
from . import views
from .views import TrackListView, TrackDetailView, TrackCreateView, TrackUpdateView, TrackDeleteView, LikeTrack, DisLikeTrack

urlpatterns = [
    path('', TrackListView.as_view(), name='home'),
    path('track/<int:pk>/', TrackDetailView.as_view(), name='track-detail'),
    path('track/<int:pk>/update/', TrackUpdateView.as_view(), name='track-update'),
    path('track/<int:pk>/delete/', TrackDeleteView.as_view(), name='track-delete'),
    path('track/new/', TrackCreateView.as_view(), name='track-upload'),
    path('like/<int:pk>', LikeTrack, name='like-track'),
    path('dislike/<int:pk>', DisLikeTrack, name='dislike-track')
]
