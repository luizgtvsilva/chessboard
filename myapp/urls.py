from django.conf.urls import url
from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path(r'^chessb/$', views.ChessBList.as_view(), name='chessb-list'),
    re_path(r'^chessb/(?P<piece_name>.+)/$', views.ChessBList.as_view(), name='piece-name-list')
]