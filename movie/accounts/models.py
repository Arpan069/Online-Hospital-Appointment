from django.db import models
from django.contrib.auth.models import User
class mobile(models.Model):
    phone=models.CharField(max_length=10,verbose_name='Phone Number')
    u=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Username')
class Doctor(models.Model):
    did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=255, verbose_name='Doctor Name')
    dmobile=models.CharField(max_length=15, verbose_name='Doctor Contact Number')
    qualification=models.CharField(max_length=255)
    specialist=models.CharField(max_length=255)
    yoe=models.CharField(max_length=2, verbose_name='Year of Experience')

class Schedule(models.Model):
    sid=models.AutoField(primary_key=True)
    time_slot=models.CharField(max_length=255, verbose_name='Timing')
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor', verbose_name='Doctor')  
    
class Appointment(models.Model):
    apid=models.AutoField(primary_key=True)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctors', verbose_name='Doctors')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient', verbose_name='Patient')
    appdate=models.DateField(verbose_name='Appointment Date')  