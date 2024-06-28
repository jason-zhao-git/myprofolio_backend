from rest_framework.routers import DefaultRouter
from guestbook.api.urls import msgrouter
from django.urls import path, include

router = DefaultRouter()

# guest msg

router.registry.extend(msgrouter.registry)

urlpatterns = [
    path('', include(msgrouter.urls))
]