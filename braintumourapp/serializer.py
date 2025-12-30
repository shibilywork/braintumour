from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

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
        fields=['date','time','status','DOCTORID']

class Appointment_Serializer_Hist(serializers.ModelSerializer):
    doct = serializers.SerializerMethodField()

    class Meta:
        model = appointmentmodel
        fields = ['date', 'time', 'status', 'doct']

    def get_doct(self, obj):
        if obj.DOCTORID:
            return obj.DOCTORID.name
        return None


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

class Complaint_Serializer(ModelSerializer):
    class Meta:
        model=complaintmodel
        fields=['complaint','date','reply']

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'