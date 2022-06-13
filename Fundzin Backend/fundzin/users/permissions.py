from .serializers import *


class has_permission:
    def isnotauth(email, finaltok):
        try:
            user = User.objects.filter(email=email).first()
            if user.finaltok == finaltok:
                return False
            return True
        except:
            return True
