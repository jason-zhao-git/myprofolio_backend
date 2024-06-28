from rest_framework.serializers import ModelSerializer
from ..models import Message

#for storing and update database
class GeneralMessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

# for guestbook display only
class GuestbookMessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['date', 'name', 'message'] 