from django.urls import path, include
from .views import *

urlpatterns = [
    path("newnotification", NewNotificationView.as_view()),
    path("getnotifications", GetNotificationsView.as_view()),
    path("getlatestnotification", GetLatestNotificationView.as_view()),
    path("getnlatestnotifications", GetNLatestNotificationsView.as_view()),
    path("getnthnotification", GetNthNotificationView.as_view()),
]
