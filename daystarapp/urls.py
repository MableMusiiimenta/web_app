from django.urls import path
from . import views
from .views import serve_js
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path("", views.index, name="index"),
    path("board.html", views.board, name="board"),
    path("dashb.html", views.dashb, name="dashb"),
    path("script.js", serve_js, name="serve_js"),
    path("baby/", views.baby, name="baby"),
    path("<int:id>/", views.view_baby, name="view_baby"),
    path("add/", views.add, name="add"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("sitter/", views.sitter, name="sitter"),
    path("adds/", views.adds, name="adds"),
    path("edits/<int:id>/", views.edits, name="edits"),
    path("deletes/<int:id>/", views.deletes, name="deletes"),
    path("view_sitter/<int:id>/", views.view_sitter, name="view_sitter"),
    path("login/", auth_views.LoginView.as_view(template_name="board.html"), name="login"),

]

urlpatterns += staticfiles_urlpatterns()