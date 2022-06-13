from django.urls import path, include
from .views import *

urlpatterns = [
    path("getupidetails", GetUPIDetailsView.as_view()),
    path("getbankdetails", GetBankDetailsView.as_view()),
    path("updateupidetails", UpdateUPIAccountDetailView.as_view()),
    path("newupiaccountdetails", NewUPIAccountDetailView.as_view()),
    path("newbankaccountdetail", NewBankAccountDetailView.as_view()),
    path("updatebankdetails", UpdateBankAccountDetailView.as_view()),
]
