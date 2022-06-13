from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import has_permission
from fundraiser.models import Fundraiser, FundraiserImages, FundraiserMilestones

"""
Views for Fundraisers
This Views contains two classes of fundraiser
"""


class NewFundraiserView(APIView):
    """
    this class is the Fundraiser View
     --> Fundraiser View:
            this one adds the new fundraiser
    """

    def post(self, request):
        """
        this function is of Fundraiser class
        takes two parameters self and request

            -> checks if the data is the requested data or not
            -> check if the fundraiser is valid or not
            -> if yes then save

        and returns the data
        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = FundraiserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class NewFundraiserMilestoneView(APIView):
    """
    this class is the Milestone View
     --> Fundraiser View:
            this class adds a new milestone
    """

    def post(self, request):
        """
        this function is of Milestone class
        takes two parameters self and request

            -> checks if the data is the requested data or not
            -> check if the fundraiser is valid or not
            -> if yes then save

        and returns the data
        """
        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        serializer = FundraiserMilestoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
