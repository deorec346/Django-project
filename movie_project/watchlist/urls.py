from django.urls import path, include
from watchlist.views import movie, movie_detail

urlpatterns = [
    path('list/', movie, name='movie'),
    path('<int:pk>', movie_detail, name='movie_detail'),
]
