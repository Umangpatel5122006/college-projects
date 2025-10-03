from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    room_no = models.CharField(max_length=5)
    address = models.TextField()
    fee_status = models.BooleanField()
    fee = models.FloatField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name
    
class Complaint(models.Model):
    Full_Name = models.CharField(max_length=100)
    Room_Number = models.CharField(max_length=5)
    Complaint_Type = models.CharField(max_length=100)
    Complaint_Details = models.TextField()
    resolved = models.BooleanField(default=False)
