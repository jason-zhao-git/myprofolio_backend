from rest_framework import viewsets, mixins
from ..models import Message
from .serializers import GuestbookMessageSerializer, GeneralMessageSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

# admin that can modify at will
class AdminMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = GeneralMessageSerializer
    permission_classes = [IsAdminUser]


#msg creation for all user
class CreateMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = GeneralMessageSerializer


#guestbook read
class GuestbookMessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.filter(show_on_guestbook=True).order_by('-date')
    serializer_class = GuestbookMessageSerializer
    pagination_class = PageNumberPagination  # Uses global settings which is 60