from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import *
from braintumourapp.models import *

# Create your views here.
class LoginPage(View):
    def get(self,request):
        return render(request,'ADMINISTRATION/login.html')
    def post(self, request):
        username1 = request.POST['username']
        password1 = request.POST['password']
        try:
            obj = loginModel.objects.get(username=username1, password=password1)
            request.session['userid'] = obj.id
            # Handle based on user type
            if obj.usertype == 'admin':
                return HttpResponse('''<script> alert("welcome back");window.location='/AdminHome'</script>''')
            

            elif obj.usertype == 'Doctor':
                return HttpResponse('''<script>alert("welcome back");window.location='/doctorhome'</script>''')

            else:
                return HttpResponse('''<script>alert("user not found");window.location='/'</script>''')
        except loginModel.DoesNotExist:
            # Handle case where login details do not exist
            return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')
    
    
class ManageDoctor(View):
    def get(self,request):
        s=doctormodel.objects.all()
        return render(request,'ADMINISTRATION/managedoctor.html',{'doctor':s})
    
class AddDoctor(View):
    def get(self,request):
        return render(request,'ADMINISTRATION/adddoctor.html')    
    def post(self,request):
        doctor=doctorform(request.POST)
        if doctor.is_valid():
            reg = doctor.save(commit=False)
            doctor= loginModel.objects.create(username=reg.name, password=request.POST['password'], usertype="Doctor")
            reg.LOGINID=doctor
            reg.save()
            return redirect('/managedoctor')
        
class Editdr(View):
    def get(self,request,id):
        a=doctormodel.objects.get(id=id)
        return render(request,'ADMINISTRATION/editdoctor.html',{'editdr':a})
    
    def post(self,request,id):
        c=doctormodel.objects.get(id=id)
        d=doctorform(request.POST,instance=c)
        if d.is_valid():
           d.save()
           return redirect('/managedoctor')   
                
        
class DeleteDoctor(View):
    def get(self, request, id):
        try:
            Usertype = doctormodel.objects.get(id=id)
            Usertype.delete()

            return HttpResponse('''<script>alert("doctor deleted successfully");
                window.location='/managedoctor'</script>''')
        except doctormodel.DoesNotExist:
            return HttpResponse('''<script>alert("doctor not found");
                window.location='/managedoctor'</script>''')

class ViewPatients(View):
    def get(self,request):
        s=patientmodel.objects.all()
        return render(request,'ADMINISTRATION/viewpatient.html',{'patients':s})
    
class ViewAppointments(View):
    def get(self,request):
        s=appointmentmodel.objects.all()
        return render(request,'ADMINISTRATION/viewappointments.html',{'appointments':s})
    
class ManageMedicines(View):
    def get(self,request):
        s=medicinemodel.objects.all()
        return render(request,'ADMINISTRATION/managemedicines.html',{'medicines':s})
    

    
class AdminHome(View):
    def get(self,request):
        return render(request,'ADMINISTRATION/adminhome.html')
    
class Addmedicine(View):
    def get(self,request):
        return render(request,'ADMINISTRATION/addmedicine.html')    
    def post(self,request):
        c=medicineform(request.POST)
        if c.is_valid():
           c.save()
           return redirect('/managemedicines')
        
class EditMedicine(View):
    def get(self,request,id):
        a=medicinemodel.objects.get(id=id)
        return render(request,'ADMINISTRATION/edit.html',{'edit':a})
    
    def post(self,request,id):
        c=medicinemodel.objects.get(id=id)
        d=medicineform(request.POST,instance=c)
        if d.is_valid():
           d.save()
           return redirect('/managemedicines')   
        
class DeleteMedicine(View):
    def get(self,request,id):
        try:
            d=medicinemodel.objects.get(id=id)
            d.delete()


            return HttpResponse('''<script>alert("medicine deleted successfully");window.location='/managemedicines'</script>''')
        except medicinemodel.DoesNotExist:
            return HttpResponse('''<script>alert("medicine not found");window.location='/managemedicines'</script>''')


class doctorhome(View):
    def get(self,request):
        return render(request,'DOCTOR/doctorhome.html')
    

class appointment(View):
    def get(self,request):
        s=appointmentmodel.objects.all()
        return render(request,'DOCTOR/appointment.html',{'doctor':s})

class notification(View):
    def get(self,request):
        s=notificationmodel.objects.all()
        return render(request,'DOCTOR/notification.html',{'notification':s})
class Addnewnotification(View):
    def get(self,request):
        return render(request,'DOCTOR/addnotification.html')    
    def post(self,request):
        d=notificationform(request.POST)
        if d.is_valid():
           d.save()
           return redirect('/notification')   

class prescription(View):
    def get(self,request):
        s=prescriptionmodel.objects.all()
        return render(request,'DOCTOR/prescription.html',{'prescription':s})
    
class post(View):
    def get(self,request):
        s=postmodel.objects.filter(DOCTORID__LOGINID__id = request.session['userid'])
        return render(request,'DOCTOR/post.html',{'post':s})
class Addnewpost(View):
    def get(self,request):
        return render(request,'DOCTOR/addpost.html')    
    def post(self,request):
        e = doctormodel.objects.get(LOGINID__id = request.session['userid'])
        d=postform(request.POST, request.FILES)
        if d.is_valid():
           c = d.save(commit=False)
           c.DOCTORID = e
           c.save()
           return redirect('/post')   
    
class acceptappointment(View):
    def get(self,request,id):
        c=appointmentmodel.objects.get(id=id)
        c.status = "appointment"
        c.save()
        return redirect('/appointment')
    
class rejectappointment(View):
    def get(self,request,id):
        c=appointmentmodel.objects.get(id=id)
        c.status = "rejected"
        c.save()
        return redirect('/appointment')
    
class AddPrescription(View):
    def get(self,request):
        return render(request,'DOCTOR/addprescription.html')
    def post(self,request):
        c=prescriptionform(request.POST)
        if c.is_valid():
           c.save()
           return redirect('/addprescription')
        