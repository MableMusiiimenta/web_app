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


    path("at_school/", views.at_school, name="at_school"),
    path("view_at_school/<int:id>/", views.view_at_school, name="view_at_school"),
    path("addd/", views.addd, name="addd"),
    path("editt/<int:id>/", views.editt, name="editt"),
    path("deletee/<int:id>/", views.deletee, name="deletee"),


    path("babyfee/", views.babyfee, name="babyfee"),
    path("view_babyfee/<int:id>/", views.view_babyfee, name="view_babyfee"),
    path("adi/", views.adi, name="adi"),
    path("edi/<int:id>/", views.edi, name="edi"),
    path("dele/<int:id>/", views.dele, name="dele"),


    path("sitter/", views.sitter, name="sitter"),
    path("adds/", views.adds, name="adds"),
    path("edits/<int:id>/", views.edits, name="edits"),
    path("deletes/<int:id>/", views.deletes, name="deletes"),
    path("view_sitter/<int:id>/", views.view_sitter, name="view_sitter"),


    path("in_school/", views.in_school, name="in_school"),
    path("view_in_school/<int:id>/", views.view_in_school, name="view_in_school"),
    path("adddd/", views.adddd, name="adddd"),
    path("edittt/<int:id>/", views.edittt, name="edittt"),
    path("deleteee/<int:id>/", views.deleteee, name="deleteee"),

    path("sitterpayment/", views.sitterpayment, name="sitterpayment"),
    path("view_sitterpayment/<int:id>/", views.view_sitterpayment, name="view_sitterpayment"),
    path("addi/", views.addi, name="addi"),
    path("edita/<int:id>/", views.edita, name="edita"),
    path("delee/<int:id>/", views.delee, name="delee"),


    path("supply/", views.supply, name="supply"),
    path("view_supply/<int:id>/", views.view_supply, name="view_supply"),
    path("addds/", views.addds, name="addds"),
    path("editts/<int:id>/", views.editts, name="editts"),
    path("deletees/<int:id>/", views.deletees, name="deletees"),


    path("doll/", views.doll, name="doll"),
    path("view_doll/<int:id>/", views.view_doll, name="view_doll"),
    path("adddds/", views.adddds, name="adddds"),
    path("edittts/<int:id>/", views.edittts, name="edittts"),
    path("deleteees/<int:id>/", views.deleteees, name="deleteees"),

    path("dollsale/", views.dollsale, name="dollsale"),
    path("view_dollsale/<int:id>/", views.view_dollsale, name="view_dollsale"),
    path("addddd/", views.addddd, name="addddd"),
    path("editttt/<int:id>/", views.editttt, name="editttt"),
    path("deleteeee/<int:id>/", views.deleteeee, name="deleteeee"),

    path("login/", auth_views.LoginView.as_view(template_name="board.html"), name="login"),

]

urlpatterns += staticfiles_urlpatterns()