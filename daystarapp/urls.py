from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("board.html", views.board, name="board"),
    path("dashb.html", views.dashb, name="dashb"),
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
]