from graphene_django.views import GraphQLView
from django.urls import path, include
from apibase.views import sdl
from . import views


urlpatterns = [
    path('graphql/sdl', sdl),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('rest/gpress/', include('gpress.api.urls')),
    path('auth/', include('rest_framework.urls')),
    path('', views.index),
]
