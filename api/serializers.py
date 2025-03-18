from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    credit_card_number = serializers.CharField()
