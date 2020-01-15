from django.db import models

# Create your models here.
class faculty (models.Model):
   facultyid=models.CharField(max_length=20,primary_key=True) 
   facultyname=models.CharField(max_length=20,null=True,blank=True)
   designation=models.CharField(max_length=20)
   joiningdate=models.CharField(max_length=20)
   qualification=models.CharField(max_length=20,null=True,blank=True)
   gender=models.CharField(max_length=10,null=True,blank=True)
   mobileno=models.IntegerField(null=True,blank=True)
   email=models.EmailField(max_length=30,null=True,blank=True)
   batchincharge=models.CharField(max_length=20,null=True,blank=True)
   blood=models.CharField(max_length=10)
   dob=models.DateField(max_length=10,null=True,blank=True)
   address=models.CharField(max_length=50,null=True,blank=True)
   password=models.CharField(max_length=20,null=True,blank=True)


class Meta:
    db_table='faculty'


class student (models.Model):
   admissionno=models.CharField(max_length=20,primary_key=True) 
   name=models.CharField(max_length=20,null=True,blank=True)
   rollno=models.IntegerField(null=True,blank=True)
   qualification=models.CharField(max_length=20,null=True,blank=True)
   gender=models.CharField(max_length=10,null=True,blank=True)
   batch=models.CharField(max_length=20,null=True,blank=True)
   dob=models.DateField(max_length=10,null=True,blank=True)
   admissiondate=models.CharField(max_length=20)
   blood=models.CharField(max_length=10)
   mobileno=models.IntegerField(null=True,blank=True)
   email=models.EmailField(max_length=30,null=True,blank=True)
   address=models.CharField(max_length=50,null=True,blank=True)
   password=models.CharField(max_length=20,null=True,blank=True)


class Meta:
    db_table='student'    


class studentleave (models.Model):
   batch=models.CharField(max_length=30,null=True,blank=True)
   name=models.CharField(max_length=30,null=True,blank=True)
   rollno=models.IntegerField() 
   leavefrom=models.CharField(max_length=50,null=True,blank=True)
   leaveto=models.CharField(max_length=50,null=True,blank=True)
   leavetype=models.CharField(max_length=30,null=True,blank=True)
   reason=models.CharField(max_length=30,null=True,blank=True)
   status=models.CharField(max_length=30)

class Meta:
    db_table='studentleave'    