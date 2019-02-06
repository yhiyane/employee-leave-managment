# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# # Create your models here.
#
# class  UserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not username:
#             raise ValueError('Users must have an username')
#         if not password:
#             raise ValueError('Users must have an password')
#
#         user = self.model(
#             username=self.model.normalize_username(username),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_staffuser(self, username, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user
#
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=20,unique=True)
#     active = models.BooleanField(default=True) # can login
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser
#     USERNAME_FIELD = 'username'
#
#     REQUIRED_FIELDS = []  # username & Password are required by default.
#
#     objects = UserManager()
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.username
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.username
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.username
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff
#
#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin
#
#     @property
#     def is_active(self):
#         "Is the user active?"
#         return self.active
