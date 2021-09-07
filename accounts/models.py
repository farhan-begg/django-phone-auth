from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from allauth.account.forms import SignupForm

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email:
            raise ValueError('email is required')
   
        if not phone:
            raise ValueError('phone number is required')

        user=self.model(
            email=self.normalize_email(email),
          
            phone=phone     
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            phone=phone,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class MyUser(AbstractUser):
    email = models.EmailField(('email address'), max_length=60,unique=True)
    phone = models.CharField(('phone'), max_length=70, unique=True)
    date_joined=models.DateTimeField(verbose_name="date time", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="date time", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=255,null=True,blank=True,unique=False)

    USERNAME_FIELD = 'email' or 'phone'
    REQUIRED_FIELDS = [ 'phone', ]

    objects=MyUserManager()

    # objects = CustomUserManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
