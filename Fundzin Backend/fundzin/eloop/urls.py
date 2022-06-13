from .views import *
from django.urls import path

urlpatterns = [
    path("eloopnewvote", EloopNewVoteView.as_view()),
    path("eloopnewuser", EloopNewUserView.as_view()),
    path("eloopnewdonation", EloopNewDonationView.as_view()),
    path("eloopnewmilestone", EloopNewMilestoneView.as_view()),
    path("eloopcheckisdonor", EloopCheckIsDonorView.as_view()),
    path("eloopnewfundraiser", EloopNewFundraiserView.as_view()),
    path("eloopactivatevoting", EloopActivateVotingView.as_view()),
    path("eloopnumberofdonors", EloopNumberOfDonorsView.as_view()),
    path("eloopgetamountraised", EloopGetAmountRaisedView.as_view()),
    path("eloopmilestonenumber", EloopCurrentMilestoneNumber.as_view()),
    path("eloopmilestonevotes", EloopNumberOfVotesForCurrentMilestone.as_view()),
    path(
        "eloopfundraisercompletioncheck", EloopFundraiserCompletionCheckView.as_view()
    ),
]
