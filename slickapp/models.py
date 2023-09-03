from django.db import models

# Create your models here.

class visitorquery(models.Model):

    services_type = [
        ("1","Project Management Tool"),
        ("2","Panel Website and Application"),
        ("3","Mobile App Development"),
        ("4","Custom Web Development"),
        ("5","Digital Marketing"),
        ("6","Community Recruitment"),
        ("7","Other"),
    ]
    
    services = models.CharField(max_length=2,choices=services_type)
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=150,default="")
    message = models.TextField(default="")
    subject = models.CharField(max_length=100,default="",null=True,blank=True)
    dateandtime = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class servicesvisitorrequest(models.Model):

    services_type = [       
        ("1","Project Management Tool"),
        ("2","Panel Website and Application"),
        ("3","Mobile App Development"),
        ("4","Custom Web Development"),
        ("5","Digital Marketing"),
        ("6","Community Recruitment"),
        ("7","Other"),
    ]
    services = models.CharField(max_length=2,choices=services_type)
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=150,default="")
    message = models.TextField(default="")
    dateandtime = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

