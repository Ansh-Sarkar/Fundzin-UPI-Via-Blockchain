from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import has_permission

# Create your views here.


class EloopNewUserView(APIView):
    """
    This class contains Post request for new User view
    """

    def post(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNewUserView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNewUserView_r",
                }
            )


class EloopNewFundraiserView(APIView):
    """
    This event loop class contains Post request for new fundraiser view
    """

    def post(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewFundraiserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNewFundraiserView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNewFundraiserView_r",
                }
            )


class EloopNewMilestoneView(APIView):
    """
    This event loop class contains Post request for new Milestone view
    """

    def post(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewFundraiserMilestoneSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNewMilestoneView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNewMilestoneView_r",
                }
            )


class EloopNewDonationView(APIView):
    """
    This event loop class contains Post request for new Donation view
    """

    def post(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewDonationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNewDonationView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNewDonationView_r",
                }
            )


class EloopCheckIsDonorView(APIView):
    """
    This event loop class contains Get request to check if the user is a donor ot not
    """

    def get(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewCheckIsDonorRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopCheckIsDonorView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopCheckIsDonorView_r",
                }
            )


class EloopGetAmountRaisedView(APIView):
    """
    This event loop class contains Get request for checking the amount of money raised
    """

    def get(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewGetAmountRaisedSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopGetAmountRaisedView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopGetAmountRaisedView_r",
                }
            )


class EloopNewVoteView(APIView):
    """
    This event loop class contains Post request for new vote view
    """

    def post(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopNewVoteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNewVoteView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNewVoteView_r",
                }
            )


class EloopActivateVotingView(APIView):
    """
    This event loop class contains Post request for activating the voting view
    """

    def post(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopActivateVotingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopActivateVotingView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopActivateVotingView_r",
                }
            )


class EloopNumberOfDonorsView(APIView):
    """
    This event loop class contains Get request for viewing the number of Donors
    """

    def get(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopGetNumberOfDonorsRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNumberOfDonorsView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNumberOfDonorsView_r",
                }
            )


class EloopNumberOfVotesForCurrentMilestone(APIView):
    """
    This event loop class contains Get request for the number of votes for the current milestone
    """

    def get(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopGetNumberOfVotesForCurrentMilestoneRequestSerializer(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopNumberOfVotesForCurrentMilestone_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopNumberOfVotesForCurrentMilestone_r",
                }
            )


class EloopCurrentMilestoneNumber(APIView):
    """
    This event loop class contains Get request for the number of current milestone
    """

    def get(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopGetCurrentMilestoneNumberRequestSerializer(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopCurrentMilestoneNumber_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopCurrentMilestoneNumber_r",
                }
            )


class EloopFundraiserCompletionCheckView(APIView):
    """
    This event loop class contains Get request for the number of votes for the current milestone
    """

    def get(self, request):

        # permissions checking
        email = request.data["user"]
        token = request.COKKIES.get("finaltok")
        if has_permission.isnotauth(email, token):
            return Response("Unauthorised", status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = EloopFundraiserCompletionCheckRequestSerializer(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(request.data)

            return Response(
                {
                    "message": "success",
                    "type": "EloopFundraiserCompletionCheckView_a",
                }
            )

        except Exception as error:
            return Response(
                {
                    "message": "error",
                    "error": str(error),
                    "type": "EloopFundraiserCompletionCheckView_r",
                }
            )
