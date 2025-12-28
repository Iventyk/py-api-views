from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreAPIView, ActorGenericView, CinemaHallViewSet, MovieViewSet

app_name = "cinema"

router = DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view()),
    path("genres/<int:pk>/", GenreAPIView.as_view()),

    path("actors/", ActorGenericView.as_view()),
    path("actors/<int:pk>/", ActorGenericView.as_view()),

    path("", include(router.urls)),
]
