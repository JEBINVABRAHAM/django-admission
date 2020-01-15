from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from faculty.models import student,faculty, studentleave 

# Create your views here.
def viewstpro(request):
     queryset=student.objects.all().filter(name=request.session['username'])
     return render(request,'student-profile.html',{'authors':queryset})  


def studetailsedit(request):
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
        student.objects.filter(name=request.session['username']).update(rollno=rollno,qualification=qualification,gender=gender,batch=batch,admissiondate=admissiondate,mobileno=mobileno,email=email,blood=blood,dob=dob,address=address,password=password)
    return render(request,'home.html')



def stueditprof(request):
     queryset=student.objects.all().filter(name=request.session['username'])
     return render(request,'student-edit.html',{'authors':queryset})  


def stuleave(request):
    if request.method=='POST':
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        leavetype=request.POST.get('leavetype')
        batch=request.POST.get('batch')
        leavefrom=request.POST.get('leavefrom')
        leaveto=request.POST.get('leaveto')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
        sl=studentleave(name=name,rollno=rollno,leavetype=leavetype,batch=batch,leavefrom=leavefrom,leaveto=leaveto,reason=reason,status=status)
        sl.save()
    return render(request,'home.html')


def stuappliedleave(request):
     queryset=studentleave.objects.all().filter(name=request.session['username'])
     return render(request,'student-applied-leave.html',{'authors':queryset})  
