from django.urls import path
from lojaa.views.HomeView import home_view
urlpatterns = [
    path("", home_view),
]