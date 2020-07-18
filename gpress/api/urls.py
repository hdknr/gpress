from django.urls import path, include
from apibase.routers import DefaultRouter
from . import viewsets

router = DefaultRouter(root_view_name='api-gpress-root')
router.register(r'post', viewsets.PostViewSet)
router.register(r'postmeta', viewsets.PostmetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
