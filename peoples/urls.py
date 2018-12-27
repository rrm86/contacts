from django.urls import re_path
from peoples import views

urlpatterns = [
    re_path(r'^people-list/$', 
        views.PeopleList.as_view(), 
        name=views.PeopleList.name),
    re_path(r'^people-detail/(?P<pk>[0-9]+)/$', 
        views.PeopleDetail.as_view(),
        name=views.PeopleDetail.name),

    re_path(r'^team-list/$', 
        views.TeamList.as_view(), 
        name=views.TeamList.name),
    re_path(r'^team-detail/(?P<pk>[0-9]+)/$', 
        views.TeamDetail.as_view(),
        name=views.TeamDetail.name),

    re_path(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]