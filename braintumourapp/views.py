from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from braintumourapp.serializer import Appointment_Serializer, Appointment_Serializer_Hist, Complaint_Serializer, Doctor_Serializer, Login_Serializer, Patient_Serializer, ReviewSerializer

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
        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserReg_api(APIView):
    def post(self, request):
        print("###################", request.data)

        user_serial = Patient_Serializer(data=request.data)
        login_serial = Login_Serializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(usertype='patient')

            # Assign the login profile to the UserTable and save the UserTable
            user_serial.save(LOGINID=login_profile)

            # Return the serialized user data in the response
            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginPageAPI(APIView):
    def post(self, request):

        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = loginModel.objects.filter(
            username=username,
            password=password
        ).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        else:
            response_dict["message"] = "success"
            response_dict["login_id"] = t_user.id
            response_dict["userType"] = t_user.usertype

        return Response(response_dict, status=status.HTTP_200_OK)
    
class ViewDoctorAPI(APIView):
    def get(self,request):
        d=doctormodel.objects.all()
        serializer=Doctor_Serializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class bookDoctor(APIView):
    def post( self, request, id):
        c=patientmodel.objects.get(LOGINID_id=id)
        serializer=Appointment_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(PATIENTID=c, status="pending")
        return Response(serializer.data, status=status.HTTP_200_OK)


class ViewBookings(APIView):
    def get( self, request, id):
        c=appointmentmodel.objects.filter(PATIENTID__LOGINID__id=id)
        serializer=Appointment_Serializer_Hist(c,many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ViewComplaint(APIView):
    def post(self, request, id):
        serializer = Complaint_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                PATIENTID=patientmodel.objects.get(LOGINID__id=id)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id):
        c = complaintmodel.objects.filter(PATIENTID__LOGINID__id=id)
        ser = Complaint_Serializer(c, many=True)
        print(ser.data)
        return Response(ser.data, status=status.HTTP_200_OK)

class ReviewPost(APIView):
    def post(self, request, id):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                USERID=patientmodel.objects.get(LOGINID__id=id)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)