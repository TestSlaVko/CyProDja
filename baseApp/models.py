from pyexpat import model
from django.db import models

# Create your models here.
class podatoci(models.Model):
    poId = models.IntegerField()
    country = models.TextField()
    Age = models.IntegerField()
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    userCourses = models.TextField(default='')
    
class coursevi(models.Model):
    title = models.TextField()
    duration = models.TextField()
    description = models.TextField()
    price = models.TextField(default='free')
    instructor = models.TextField(default="instructor 1")
    dificulty = models.TextField(default="begginer")
    testing = models.BooleanField(default=False)




class UserCourses(models.Model):
    user = models.TextField()
    courses= models.TextField()

class UserNotes(models.Model):
    user = models.TextField()
    subject = models.TextField()
    note = models.TextField()