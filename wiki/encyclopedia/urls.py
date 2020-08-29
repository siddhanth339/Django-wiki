from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search/', views.search, name = "search"),
    path("newPage/", views.newPage, name = "newPage"),
    path("<str:name>", views.TITLE, name = "TITLE"),
    path("edit/<str:name>", views.edit, name = "edit")
    
]
