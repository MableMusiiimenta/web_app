from django.urls import path

from . import views
from .views import admin_login
from .views import serve_js
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import search_results
from .views import search_another_model

urlpatterns = [
    path("", views.index, name="index"),
    path('admin_login/', admin_login, name='admin_login'),

    path("dashb/", views.dashb, name="dashb"),
    path('search/', search_results, name='search_results'),
    path('search_another_model/', search_another_model, name='search_another_model'),

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

    path("monthlyfee/", views.monthlyfee, name="monthlyfee"),
    path("view_monthlyfee/<int:id>/", views.view_monthlyfee, name="view_monthlyfee"),
    path("addt/", views.addt, name="addt"),
    path("eddt/<int:id>/", views.eddt, name="eddt"),
    path("delet/<int:id>/", views.delet, name="delet"),


    path("sitter/", views.sitter, name="sitter"),
    path("adds/", views.adds, name="adds"),
    path("edits/<int:id>/", views.edits, name="edits"),
    path("deletes/<int:id>/", views.deletes, name="deletes"),
    path("view_sitter/<int:id>/", views.view_sitter, name="view_sitter"),


    path("shift/", views.shift, name="shift"),
    path("view_shift/<int:id>/", views.view_shift, name="view_shift"),
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
    path("logged_out/", views.logout_view, name="logged_out"),
]

urlpatterns += staticfiles_urlpatterns()