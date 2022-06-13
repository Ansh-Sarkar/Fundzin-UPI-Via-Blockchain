import os
import json
import random
import jwt, datetime
from PIL import Image
from uuid import uuid4
from pathlib import Path
from .serializers import *
from jsonmerge import merge
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import has_permission
from notifications.models import Notification
from rest_framework.exceptions import AuthenticationFailed


"""
        Views for Notification
        This Views contains two classes of Notification
"""


class NewNotificationView(APIView):
    """
    Class for notification view that checks for any new notification POST request
    """

    def post(self, request):
        """
        this fuction takes two arguments

            ->self,request

            ->checks if the data is valid

            ->saves it

        returns the response
        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = NotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data["img"])
        file_path = os.getcwd().replace("\\", "/") + serializer.data["img"]
        print(file_path)
        im = Image.open(file_path)
        im.show()
        return Response(serializer.data)


class GetNotificationsView(APIView):
    """
    Class for notification view that checks for notification GET request
    """

    def get(self, request):
        """
        this fuction takes two arguments

            ->self,request

            ->checks if the data is valid

            -> checks if the number of notification is less than 1

                Returns a message: "No notifications found for the specified user !"

            ->saves it

        returns the response
        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = GetNotificationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data["email"])
        notification_list = Notification.objects.filter(
            sent_to=serializer.data["email"]
        )
        print(notification_list)
        data = []
        if len(notification_list) < 1:
            return Response(
                {"message": "No notifications found for the specified user !"}
            )
        serialized_notification = NotificationSerializer(notification_list[0])
        for i in range(0, len(notification_list)):
            serialized_notification = NotificationSerializer(notification_list[i])
            data.append(serialized_notification.data)
        print(serialized_notification.data)
        return Response(data)


class GetLatestNotificationView(APIView):
    """
    Class for notification view that gets the latest notification (GET REQUEST)
    """

    def get(self, request):
        """
        this fuction takes two arguments

            ->self,request

            ->checks if the data is valid

            -> checks if the number of latest notification is less than 1

                Returns a message: "No notifications found for the specified user !"

            ->saves it

        returns the response
        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = GetNotificationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data["email"])
        latest_notification = Notification.objects.filter(
            sent_to=serializer.data["email"]
        )
        if len(latest_notification) < 1:
            return Response(
                {"message": "No notifications exist for the current user !"}
            )
        latest_notification = latest_notification[len(latest_notification) - 1]
        return Response(NotificationSerializer(latest_notification).data)


class GetNthNotificationView(APIView):
    """
    this fuction takes two arguments

        ->self,request

        ->checks if the data is valid

        -> checks if the number of latest notification is less than 1

             Returns a message: "No notifications found for the specified user !"

        ->saves it

        returns the response
    """

    def get(self, request):
        """
        this fuction takes two arguments

            ->self,request

            ->checks if the data is valid

            -> checks if the number of latest notification is less than 1

                Returns a message: "No notifications found for the specified user !"

            ->saves it

        returns the response
        """

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = GetNLatestNotificationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data["email"])
        latest_notification = Notification.objects.filter(
            sent_to=serializer.data["email"]
        )
        if len(latest_notification) < 1:
            return Response(
                {"message": "No notifications exist for the current user !"}
            )
        elif (
            serializer.data["n"] > len(latest_notification) or serializer.data["n"] < 1
        ):
            return Response({"message": "warning : invalid positional argument !"})
        latest_notification = latest_notification[serializer.data["n"] - 1]
        return Response(NotificationSerializer(latest_notification).data)


class GetNLatestNotificationsView(APIView):
    """
    Class for notification view that gets the Nth notification (GET REQUEST)
    """

    def get(self, request):
        """
        this fuction takes two arguments

            ->self,request

            ->checks if the data is valid

            -> checks if the number of latest notification is less than 1

                Returns a message: "No notifications found for the specified user !"

            ->saves it

        returns the response
        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = GetNLatestNotificationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data["email"])
        data = []
        latest_notifications = Notification.objects.filter(
            sent_to=serializer.data["email"]
        )
        if len(latest_notifications) < 1:
            return Response(
                {"message": "No notifications exist for the current user !"}
            )
        elif len(latest_notifications) < serializer.data["n"]:
            data.append({"message": "warning : less than n notifications found !"})
        else:
            l = len(latest_notifications)
            latest_notifications = latest_notifications[l - serializer.data["n"] : l]

        for i in range(0, len(latest_notifications)):
            serialized_notification = NotificationSerializer(latest_notifications[i])
            data.append(serialized_notification.data)

        return Response(data)
