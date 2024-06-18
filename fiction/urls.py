
from django.urls import path

from . import views


app_name = "fiction"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:fiction_code>/", views.detail, name="detail"),
]
