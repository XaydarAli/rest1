from django.urls import path
from .views import ArtistAPIView,ArtistAPIMobileView,AlbumAPIView,SongAPIView
urlpatterns = [
    path('artists/', ArtistAPIView.as_view(), name="artists"),
    path('artist-mobile/', ArtistAPIMobileView.as_view(), name="artist-mobile"),
    path('albums/', AlbumAPIView.as_view(), name="albums"),
    path('songs/', SongAPIView.as_view(), name="songs"),
]