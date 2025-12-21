"""
URL configuration for braintumour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from braintumourapp.views import *

urlpatterns = [
    path('',LoginPage.as_view(),name='login'),
    path('managedoctor',ManageDoctor.as_view(),name='managedoctor'),
    path('viewpatient',ViewPatients.as_view(),name='viewpatient'),
    path('viewappointments',ViewAppointments.as_view(),name='viewappointments'),
    path('managemedicines',ManageMedicines.as_view(),name='managemedicines'),
    path('adddoctor',AddDoctor.as_view(),name='adddoctor'),
    path('AdminHome',AdminHome.as_view(),name='adminhome'),
    path('DeleteDoctor/<int:id>',DeleteDoctor.as_view(),name='DeleteDoctor'),
    path('addmedicine',Addmedicine.as_view(),name='addmedicine'),
    path('edit/<int:id>',EditMedicine.as_view(),name='edit'),
    path('DeleteMedicine/<int:id>',DeleteMedicine.as_view(),name='DeleteMedicine'),
    path('editdoctor/<int:id>',Editdr.as_view(),name='editdoctor'),

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    path('doctorhome',doctorhome.as_view(),name='doctorhome'),
    path('appointment',appointment.as_view(),name='appointment'),
    path('notification',notification.as_view(),name='notification'),
    path('post',post.as_view(),name='post'),
    path('prescription',prescription.as_view(),name='prescription'),
    path('acceptappointment/<int:id>',acceptappointment.as_view(),name='acceptappointment'),
    path('rejectappointment/<int:id>',rejectappointment.as_view(),name='rejectappointment'),
    path('addprescription',AddPrescription.as_view(),name='addprescription'),
    path('Addnewnotification',Addnewnotification.as_view(),name='Addnewnotification'),
    path('Addnewpost',Addnewpost.as_view(),name='Addnewpost'),
]
