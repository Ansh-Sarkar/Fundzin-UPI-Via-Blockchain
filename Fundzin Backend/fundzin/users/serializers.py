from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """
        serializer class for user

        models consists of fields
            (int) id
            (String) first_name
            (String) last_name
            (String) email
            (String) password

        """

        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "user_type"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        This function takes two Arguments

            self, validated_data

            function checks if the password is not null,

            it sets the password

            saves the instance

        returns the instance
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class GetRequestSerializer(serializers.Serializer):
    """
    -> (int) id: To keep track of Bank Detail

    -> (String of length 255) user: Email of the user
    """

    id = serializers.IntegerField(read_only=True)
    user = serializers.EmailField(required=True, allow_blank=False, max_length=255)
