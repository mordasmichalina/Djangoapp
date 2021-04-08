from django.conf.urls import url, include
from rest_framework.authtoken.views import ObtainAuthToken
from .views import UserViewSet, UserRegisterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', ObtainAuthToken.as_view()),
    url(r'^register/', UserRegisterViewSet.as_view())
]