from django.contrib import admin

from braintumourapp.models import *

# Register your models here.
admin.site.register(loginModel)
admin.site.register(doctormodel)
admin.site.register(patientmodel)
admin.site.register(appointmentmodel)
admin.site.register(medicinemodel)
admin.site.register(prescriptionmodel)
admin.site.register(notificationmodel)
admin.site.register(postmodel)