import json
import random
import jwt, datetime
from uuid import uuid4
from .serializers import *
from jsonmerge import merge
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import has_permission
from notifications.models import Notification
from rest_framework.exceptions import AuthenticationFailed


class NewBankAccountDetailView(APIView):
    """Class to create POST request for NewBanAccountDetailView"""

    def post(self, request):
        """
        this functiont takes two Arguments

            -self,request

            -checks if the data is valid

            -if length is more than 0

                returns "warning : pre-existing upi id found . kindly update it "

            -if account numbers doesnot match

                returns "warning : bank account numbers dont match . kindly retry."


        returns the response
        """
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")

        # permissions checking

        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = BankDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = BankDetail.objects.filter(user=serializer.validated_data["user"])
        if len(check) > 0:
            return Response(
                {"message": "warning : pre-existing upi id found . kindly update it ."}
            )
        elif (
            serializer.validated_data["bank_account_number"]
            != serializer.validated_data["bank_confirm_account_number"]
        ):
            return Response(
                {"message": "warning : bank account numbers dont match . kindly retry."}
            )
        else:
            serializer.save()
            return Response(serializer.data)


class UpdateBankAccountDetailView(APIView):
    """
    Class to UPDATE BankAccountDetail
    """

    def patch(self, request):
        """
        this function accepts two Arguments

            self, request

            checks if the data is valid

            if everything goes fine

            the functions returns response and updates
            "updated records successfully !"

        """

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = BankDetailSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            current = BankDetail.objects.get(user=serializer.validated_data["user"])
        except:
            return Response(
                {
                    "message": "oops ! something went wrong . kindly recheck the entered username and try again"
                }
            )
        if serializer.is_valid():
            serializer.update(current, serializer.validated_data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)
        return Response({"message": "updated records successfully !"})


class NewUPIAccountDetailView(APIView):
    """
    Class to UPDATE BankAccountDetail
    """

    def post(self, request):
        """
        this function accepts two Arguments

            self, request

            checks if the data is valid

            if UPI already exists:
            message": "warning : pre-existing upi id found . kindly update it .

        returns the response

        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = UPIDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = UPIDetail.objects.filter(user=serializer.validated_data["user"])
        if len(check) > 0:
            return Response(
                {"message": "warning : pre-existing upi id found . kindly update it ."}
            )
        else:
            serializer.save()
            return Response(serializer.data)


class UpdateUPIAccountDetailView(APIView):
    """
    Class to UPDATE UPI acount detail
    """

    def patch(self, request):
        """
        this function accepts two Arguments

            self, request

            checks if the data is valid

            checks if everything is correct

                if not then

                    "message": "oops ! something went wrong . kindly recheck the entered username and try again"

                if yes then

                    "message": "updated records successfully !"

        returns the response

        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = UPIDetailSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            current = UPIDetail.objects.get(user=serializer.validated_data["user"])
        except:
            return Response(
                {
                    "message": "oops ! something went wrong . kindly recheck the entered username and try again"
                }
            )
        if serializer.is_valid():
            serializer.update(current, serializer.validated_data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)
        return Response({"message": "updated records successfully !"})


class GetBankDetailsView(APIView):
    """
    Class to Get the the detais of the bank
    """

    def get(self, request):
        """
        this function accepts two Arguments

            self, request

            checks if the data is valid

        returns the response

        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = GetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            current = BankDetail.objects.get(user=serializer.validated_data["user"])
        except:
            return Response(
                {
                    "message": "oops ! something went wrong . kindly recheck the entered username and try again"
                }
            )
        if serializer.is_valid():
            return Response(BankDetailSerializer(current).data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)


class GetUPIDetailsView(APIView):
    """
    Class to Get the the UPI details
    """

    def get(self, request):
        """
        this function accepts two Arguments

            self, request

            checks if the data is valid

        returns the response

        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = GetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            current = UPIDetail.objects.get(user=serializer.validated_data["user"])
        except:
            return Response(
                {
                    "message": "oops ! something went wrong . kindly recheck the entered username and try again"
                }
            )
        if serializer.is_valid():
            return Response(UPIDetailSerializer(current).data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)
