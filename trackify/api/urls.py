from django.urls import path
from .views import TrackView

urlpatterns = [
    path('home', TrackView.as_view()),
]