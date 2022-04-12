from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.
class Region(models.Model):
    city = models.CharField(max_length=100, primary_key=True)
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.city

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=100, null=False, default="a@gmail.com")
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    aadhar_no = models.BigIntegerField(max_length=12, primary_key=True)
    blood_group = models.CharField(max_length=3)
    phone_number = models.BigIntegerField(max_length=10)
    address = models.CharField(max_length=100)
    hemoglobin = models.FloatField(default=0)
    city = models.ForeignKey(Region, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(age__gte=18), name='age_check'),
            models.CheckConstraint(check=Q(age__lte=65), name='age_check_high'),
            models.CheckConstraint(check=Q(hemoglobin__gte=13), name='hemoglobin_check'),
        ]
    def __str__(self):
        return self.name

class Receiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=100,null=False,default="a@gmail.com")
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    aadhar_no = models.BigIntegerField(max_length=12, primary_key=True)
    blood_group = models.CharField(max_length=3)
    phone_number = models.BigIntegerField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
