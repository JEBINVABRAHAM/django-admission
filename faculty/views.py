from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from faculty.models import faculty,student

# Create your views here.
def display1(request):
    if request.method=='POST':
        username=request.POST.get('staffAccount')
        password=request.POST.get('staffPassword')
        username=str(username)
        password=str(password)
        u=faculty.objects.filter(facultyname=username,password=password)
        if u.count()==1:
            request.session['username']=username
            return render(request,'faculty-login.html')
        else:
            u2=student.objects.filter(name=username,password=password)      
            if u2.count()==1:
                 request.session['username']=username
                 return render(request,'home.html')    
            else:
              return HttpResponse('login unsuccesfull')      
       
def logout_view(request):
    logout(request)
    return render(request,'index.html') 


def viewfacpro(request):
     queryset=faculty.objects.all().filter(facultyname=request.session['username'])
     return render(request,'facultyprofile.html',{'authors':queryset})  

def facdetailsedit(request):
    if request.method=='POST':
        facultyid=request.POST.get('facultyid')
        facultyname=request.POST.get('facultyname')
        designation=request.POST.get('designation')
        joiningdate=request.POST.get('joiningdate')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        mobileno=request.POST.get('mobileno')
        email=request.POST.get('email')
        batchincharge=request.POST.get('batchincharge')
        blood=request.POST.get('blood')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        password=request.POST.get('password')       
        faculty.objects.filter(facultyname=request.session['username']).update(address=address,gender=gender,email=email,qualification=qualification,mobileno=mobileno, batchincharge=batchincharge,password=password)
    return render(request,'faculty-login.html')


def faceditprof(request):
     queryset=faculty.objects.all().filter(facultyname=request.session['username'])
     return render(request,'faculty-profile-edit.html',{'authors':queryset})  


def display(request):
    if request.method=='POST':
        admissionno=request.POST.get('admissionno')
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        batch=request.POST.get('batch')
        admissiondate=request.POST.get('admissiondate')
        mobileno=request.POST.get('mobileno')
        email=request.POST.get('email')
        blood=request.POST.get('blood')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        password=request.POST.get('password')
        a=student(admissionno=admissionno,name=name,rollno=rollno,qualification=qualification,gender=gender,batch=batch,admissiondate=admissiondate,mobileno=mobileno,email=email,blood=blood,dob=dob,address=address,password=password)
        a.save()
    return render(request,'faculty-login.html')

def facstuddetails(request):
     queryset=student.objects.all()
     return render(request,'faculity_home_batch.html',{'authors':queryset})  
