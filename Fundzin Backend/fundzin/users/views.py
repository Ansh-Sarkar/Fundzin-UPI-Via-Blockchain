import random
import jwt, datetime
from uuid import uuid4
from .serializers import *
from eloop.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
class RegisterView(APIView):
    """
    Class for Register view, contains a post request

    -> used to register a user
    """

    def post(self, request):
        """
        This function takes two Arguments

            self, request
            checks if the data is valid
            saves the data

        returns the response
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserExistsView(APIView):
    """
    Class for User Exists view, contains a get request

    -> checks if the user exists or not
    """

    def get(self, request):
        """
        This function takes two Arguments

            self, request
            checks if the data is valid
            checks if data exists or not

        returns the response
        """
        serializer = GetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            account = User.objects.get(email=serializer.validated_data["user"])
        except:
            return Response({"exists?": "false"})
        return Response({"exists?": "true"})


class LoginView(APIView):
    """
    Class for Login view, contains a post request

    -> This class contains a function for Login
    """

    def post(self, request):
        """

        this function accepts two arguments:

            self, request

            enters email

            enters password

            checks if the user is found or not

            checks if the password is correct or not

            if email and password are correct
                4 digit otp is generated

            if otp is correct

        response is returned
        """
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            "iat": datetime.datetime.utcnow(),
        }
        # otp creation
        secret = str(random.randint(1000, 9999))
        print("Your OTP is : ", secret)
        # jwt created based on otp
        token = jwt.encode(payload, secret, algorithm="HS256").decode("utf-8")
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        try:
            secret = request.data.get("otp")
        except:
            AuthenticationFailed("Wrong OTP")
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload = jwt.decode(token, secret, alogorith=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        except jwt.InvalidSignatureError:
            raise AuthenticationFailed("Invalid OTP")
        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)
        # save authenticated attribute true
        user.isauthenticated = True
        # create a final token after 2fa
        tk = uuid4()
        user.finaltok = tk
        user.save()
        # save the token in db for further permissions
        response = Response()
        # return the token to the user
        response.data = {"data": serializer.data, "token": tk}
        return response
