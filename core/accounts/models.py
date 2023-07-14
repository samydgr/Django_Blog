from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("the Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True :
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True :
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email,password,**extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email
        
class Profile(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     first_name = models.CharField(max_length=250)
     last_name = models.CharField(max_length=250)
     image = models.ImageField(blank=True,null=True)
     description = models.TextField()
     created_date = models.DateTimeField(auto_now_add=True)
     updated_date = models.DateTimeField(auto_now=True)
     def __str__(self):
        return self.user.email
@receiver(post_save, sender=User)
def save_profile(sender, instance,created,**kwargs):
    if created:
       Profile.objects.create(user = instance)