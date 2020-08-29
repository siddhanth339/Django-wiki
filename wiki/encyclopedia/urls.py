from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.TITLE, name = "TITLE"),
    path('search/', views.search, name = "search"),
    path("newPage/", views.newPage, name = "newPage")
]
