from django.db import models

# Create your models here.
class loginModel(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

class doctormodel(models.Model):
    LOGINID=models.ForeignKey(loginModel,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    specialisation=models.CharField(max_length=100,null=True,blank=True)
    hospitalname=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)

class patientmodel(models.Model):
    LOGINID=models.ForeignKey(loginModel,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)

class appointmentmodel(models.Model):
    PATIENTID=models.ForeignKey(patientmodel,on_delete=models.CASCADE,null=True,blank=True)
    DOCTORID=models.ForeignKey(doctormodel,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)

class medicinemodel(models.Model):
    DOCTORID=models.ForeignKey(doctormodel,on_delete=models.CASCADE,null=True,blank=True)
    medicine=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)

class prescriptionmodel(models.Model):
    PATIENTID=models.ForeignKey(patientmodel,on_delete=models.CASCADE,null=True,blank=True)
    DOCTORID=models.ForeignKey(doctormodel,on_delete=models.CASCADE,null=True,blank=True)
    prescription=models.CharField(max_length=100,null=True,blank=True)
    medicine=models.CharField(null=True,blank=True)

class postmodel(models.Model):
    DOCTORID=models.ForeignKey(doctormodel,on_delete=models.CASCADE,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    image=models.FileField(null=True,blank=True)

class notificationmodel(models.Model):
    notification=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(auto_now_add=True)




