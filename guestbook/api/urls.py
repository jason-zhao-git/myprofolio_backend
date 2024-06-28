from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuestbookMessageViewSet, CreateMessageViewSet, AdminMessageViewSet

msgrouter = DefaultRouter()
msgrouter.register(r'admin/messages', AdminMessageViewSet, basename='admin-messages')
msgrouter.register(r'createmsgs', CreateMessageViewSet, basename='createmsg')
msgrouter.register(r'guestbook', GuestbookMessageViewSet, basename='guestbook')

urlpatterns = [
    path('', include(msgrouter.urls)),
]
