from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.Serializer):
    """
    This is the serializer class for Notification:
        it contains:
    -> (int) id: To keep track of notification

    -> (String of length 255) sent_to: Email id of the reciever

    -> (String of length 255) title: A title to be shown on the Notification

    -> (String) message: A message to be shown on the Notification

    -> (String) img: Image for the notification



    """

    id = serializers.IntegerField(read_only=True)
    sent_to = serializers.EmailField(required=True, allow_blank=False)
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    message = serializers.CharField(required=True, allow_blank=False)
    img = serializers.ImageField(max_length=None, allow_empty_file=False)

    def create(self, validated_data):
        """
        function to create the notification serializer

            takes two Arguments
                self , validated data

        returns the serializer
        """
        return Notification.objects.create(**validated_data)


class GetNotificationsSerializer(serializers.Serializer):
    """
    Serializer class to get the notification

        -> (int) id: To keep track of notification

        -> (String of length 255) email: Email id

    """

    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True, allow_blank=False)


class GetNLatestNotificationsSerializer(serializers.Serializer):
    """
    Serializer class to get the notification

        -> (int) id: To keep track of notification

        -> (String of length 255) email: Email id

        -> (int) n: The number of notification the user wants

    """

    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True, allow_blank=False)
    n = serializers.IntegerField(required=True)
