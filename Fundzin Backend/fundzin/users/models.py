from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class User(AbstractUser):
    """
    (String of size 200) first_name: First name of the user
    (String of size 200) last_name: Last name of the user
    (String of size 255) email: Email of the user
    (String of size 25) user_type: Gender of the user
    (String of size 255) password: Password of the user
    (String of size 6) otp: OTP of the user
    (boolean) authenticated: Is the user authenticated or not
    (String of size 255) finaltok: Token
    (String) username: User name of the user
    (boolean) creation_transaction_completed: Is the creation for the transaction completed or not
    (String) USERNAME_FIELD: Email
    (String) REQUIRED_FIELDS: []
    """

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    user_type = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    otp = models.CharField(max_length=6)
    authenticated = models.BooleanField(default=False)
    finaltok = models.CharField(max_length=255, default="no-token")
    username = None
    creation_transaction_completed = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
