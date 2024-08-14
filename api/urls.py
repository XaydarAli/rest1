from rest_framework import routers
#from .views import ArtistAPIView,ArtistAPIMobileView,AlbumAPIView,AlbumDetailAPIView,ArtistDetailAPIView,SongAPIView,SongDetailAPIView
from .views import SongAPIViewSET,AlbumAPIViewSET,ArtistAPIViewSET
from .views import ArtistMobileAPIViewSET,AlbumMobileAPIViewSET,SongMobileAPIViewSET
from .views import ArtisttelebotAPIViewSET,AlbumtelebotAPIViewSET,SongtelebotAPIViewSET
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path,include
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
    openapi.Info(
        title="Spotify API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'songs',SongAPIViewSET,basename='songs')
router.register(r'albums',AlbumAPIViewSET,basename='albums')
router.register(r'artists',ArtistAPIViewSET,basename='artists')
router.register(r'artists-mobile',ArtistMobileAPIViewSET,basename='artists-mobile')
router.register(r'albums-mobile',AlbumMobileAPIViewSET,basename='albums-mobile')
router.register(r'songs-mobile',SongMobileAPIViewSET,basename='songs-mobile')

router.register(r'artists-telebot',ArtisttelebotAPIViewSET,basename='artists-telebot')
router.register(r'albums-telebot',AlbumtelebotAPIViewSET,basename='albums-telebot')
router.register(r'songs-telebot',SongtelebotAPIViewSET,basename='songs-telebot')

urlpatterns = [
    # path('artists/', ArtistAPIView.as_view(), name="artists"),
    # path('artists/<int:id>/', ArtistDetailAPIView.as_view(), name="artist-detail"),
    # path('artist-mobile/', ArtistAPIMobileView.as_view(), name="artist-mobile"),
    # path('albums/', AlbumAPIView.as_view(), name="albums"),
    # path('albums/<int:id>/', AlbumDetailAPIView.as_view(), name="album-detail"),
    # path('songs/', SongAPIView.as_view(), name="songs"),
    # path('songs/<int:id>/', SongDetailAPIView.as_view(), name="song-detail"),

    path('api-token-auth/', obtain_auth_token),

    path('',include(router.urls)),
]

urlpatterns+=[
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
