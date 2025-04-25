from user_app.models import User
from chat_app.serializer import ChatContentrSerializertoUser
from rest_framework import serializers

class UserChatContentSerializer2(serializers.ModelSerializer):
    chat_contents = ChatContentrSerializertoUser(many=True,read_only=True)

    class Meta:
        model = User
        fields = ['chat_contents','id']

