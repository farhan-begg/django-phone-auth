from django.contrib.auth import user_login_failed
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from accounts.models import MyUser


class AuthBackend(ModelBackend):
    """
    Authenticates the User with email or by Phone Number
    """

    def authenticate(self, request, **kwargs):
        email_or_phone = kwargs.get('email_or_phone')
        password = kwargs.get('password')
        try:
            # Check if a user is available with given email or phone number.
            # Email will be the first priority.
            # Phone Number will be second priority.
            user = MyUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
            if user.check_password(password) is True:
                return user
        except MyUser.DoesNotExist:
            user_login_failed.send(sender=__name__, request=request)
