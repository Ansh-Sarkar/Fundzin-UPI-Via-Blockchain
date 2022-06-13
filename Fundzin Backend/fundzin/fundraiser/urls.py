"""
    URL ENDPOINTS FOR THE FUNDZIN > FUNDRAISER MODULE
"""

from django.urls import path, include
from .views import *


class newfundraiser:
    """
    Base API URL : http://127.0.0.1:8000/fundraiser/

    Specific API Endpoint : http://127.0.0.1:8000/fundraiser/newfundraiser/

    METHODS : [POST]

    returns (the values passed to the API are re returned upon successfull addition to database)
    """

    user = ""
    """(Email)   user                               : An email field which is used to input the Email of the fundraiser"""
    fundraiser_domain = ""
    """(String)  fundraiser_domain                  : fundraiser domain for putting the domain of the fundraiser"""
    creator_location = ""
    """(String)  creator_location                   : location of the fundraiser"""
    contact_number_country_code = ""
    """(String)  contact_number_country_code        : a field for country code which has a max length of 5 """
    contact_number = ""
    """(String)  contact_number                     : contact number of fundraser 10 digit"""
    title = ""
    """(String)  title                              : A title to be shown on the Application"""
    cause = ""
    """(String)  cause                              : Reason why the fundraiser wants funds in a nutshell"""
    story = ""
    """(String)  story                              : An elaborated version for why the fundraiser wants funding"""
    target_amount = ""
    """-> (int)     target_amount                      : Money required to fullfill the goal of the user"""
    political_or_religious_inclination = ""
    """(boolean) political_or_religious_inclination : Is the fundraised amount going to get involved in any sort of political or religius activity?"""
    add_upi = ""
    """(boolean) add_upi                            : Add the upi id to transfer the money"""


class newfundraisermilestone:
    """
    Base API URL : http://127.0.0.1:8000/fundraiser/

    Specific API Endpoint : http://127.0.0.1:8000/fundraiser/newfundraisermilestone/

    METHODS : [POST]

    returns (the values passed to the API are re returned upon successfull addition to database)
    """

    id = ""
    """(Integer) id"""
    user = ""
    """(String of length 255) user                     : An email field which is used to input the Email of the fundraiser"""
    milestone_id = ""
    """(String of length 255) milestone_id             : An id for milestone"""
    milestone_title = ""
    """(String of length 255) milestone_title          : Title for milestone to be displayed"""
    milestone_desc = ""
    """(String of length 255) milestone_desc           : Milestone description"""
    milestone_release_amount = ""
    """(String of length 255) milestone_release_amount : Money after completion of each milestone"""


urlpatterns = [
    path("newfundraiser", NewFundraiserView.as_view()),
    path("newfundraisermilestone", NewFundraiserMilestoneView.as_view()),
]
"""
    Contains the API Endpoints present under the http://127.0.0.1:8000/fundraiser/ BASE ENDPOINT
"""
