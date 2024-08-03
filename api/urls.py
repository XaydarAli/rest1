from django.urls import path
from .views import ArtistAPIView,ArtistAPIMobileView,AlbumAPIView,SongAPIView,SongDetailAPIView,AlbumDetailAPIView,ArtistDetailAPIView
urlpatterns = [
    path('artists/', ArtistAPIView.as_view(), name="artists"),
    path('artists/<int:id>/', ArtistDetailAPIView.as_view(), name="artist-detail"),
    path('artist-mobile/', ArtistAPIMobileView.as_view(), name="artist-mobile"),
    path('albums/', AlbumAPIView.as_view(), name="albums"),
    path('albums/<int:id>/', AlbumDetailAPIView.as_view(), name="album-detail"),
    path('songs/', SongAPIView.as_view(), name="songs"),
    path('songs/<int:id>/', SongDetailAPIView.as_view(), name="song-detail"),
]