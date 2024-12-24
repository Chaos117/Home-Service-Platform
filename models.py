from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class UserProfile(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=13)
    address = models.TextField()
    gender = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic = models.FileField(upload_to='user_profiles/')

class Worker(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=13)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)  # Corrected this line
    gender = models.CharField(max_length=250)
    designation = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to='worker_profiles/')
    acc_activation = models.BooleanField(default=False)
    availability_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Country(models.Model):
    name = models.CharField(max_length=150)

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

class ServiceCategory(models.Model):
    img = models.ImageField(upload_to='category_imgs/')
    name = models.CharField(max_length=255)
    description = models.TextField()

class ServiceRequest(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    problem_description = models.TextField()
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pin = models.CharField(max_length=10)
    house_no = models.CharField(max_length=20)
    landmark = models.TextField(null=True)
    contact = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    date_of_request = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

class Feedback(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    employ = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_token = models.CharField(max_length=1000)
