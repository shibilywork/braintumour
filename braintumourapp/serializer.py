from rest_framework.serializers import ModelSerializer

from braintumourapp.models import *

class Login_Serializer(ModelSerializer):
    class Meta:
        model=loginModel
        fields=['username','password','usertype']

class Doctor_Serializer(ModelSerializer):
    class Meta:
        model=doctormodel
        fields=['id','name','phone','address','gender','specialisation','hospitalname','age']

class Patient_Serializer(ModelSerializer):
    class Meta:
        model=patientmodel  
        fields=['name','phone','gender','age','email']

class Appointment_Serializer(ModelSerializer):
    class Meta:
        model=appointmentmodel
        fields=['date','time','status']

class Prescription_Serializer(ModelSerializer):
    class Meta:
        model=prescriptionmodel
        fields=['prescription','medicine']

class Post_Serializer(ModelSerializer):
    class Meta:
        model=postmodel
        fields=['description','date','image']

class Notification_Serializer(ModelSerializer):
    class Meta:
        model=notificationmodel
        fields=['notification','date']