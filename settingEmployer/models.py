from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
from employee_leave_management import settings


class BusinessUnit(models.Model):
    be_Code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Position(models.Model):
    position_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.libelle


class Team(models.Model):
    team_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cin_code = models.CharField(max_length=10, unique=True, null=True)
    birth_date = models.DateField(null=True)
    hire_date = models.DateField(null=True)
    email = models.EmailField(max_length=100, blank=False, unique=True, null=True)
    cnss_code = models.CharField(max_length=30, unique=True, null=True)
    experience_years_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    leave_days_number = models.FloatField(null=True, blank=True)
    resignation_date = models.DateField(null=True, blank=True)
    be = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, null=True)
    positon = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    tag_manager = models.BooleanField(default=False)
    team = models.ManyToManyField(Team)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
