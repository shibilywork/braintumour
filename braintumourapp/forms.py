from django.forms import *

from .models import *



class doctorform(ModelForm):
    class Meta:
        model=doctormodel
        fields='__all__'

class medicineform(ModelForm):
    class Meta:
        model=medicinemodel
        fields='__all__'        

class prescriptionform(ModelForm):
    class Meta:
        model=prescriptionmodel
        fields='__all__'         

class notificationform(ModelForm):
    class Meta:
        model=notificationmodel
        fields='__all__'   

class postform(ModelForm):
    class Meta:
        model=postmodel
        fields='__all__'   