from django.urls import path, include
from .views import *

urlpatterns = [
    path("user", UserView.as_view()),
    path("login", LoginView.as_view()),
    path("register", RegisterView.as_view()),
    path("checkuserexistence", UserExistsView.as_view()),
]
