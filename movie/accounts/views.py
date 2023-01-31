from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from accounts.models import mobile,Schedule,Doctor,Appointment
def index(request):
    
    return render(request,'index.html')

def news(request):
    return render(request,'news.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        surname=request.POST.get('last')
        username=request.POST.get('username')
        ph=request.POST.get('phone')
        email=request.POST.get('mail')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"This username already exists")
                return redirect('/signup/')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"This email already exists")
                return redirect('/signup/')  
            else:
                user=User.objects.create_user(username=username,first_name=name,last_name=surname,email=email,password=pass1) 
                user.save()
                m=mobile(u=user,phone=ph)
                m.save()
                if user is not None:
                    
                    login(request,user)
                    messages.success(request,'Account Created. Please Login!',extra_tags='success')

                    return redirect('/Login/')
                else:
                    messages.error(request,"Unsuccessfull")
                    return redirect('/signup/')
        else:
            messages.error(request,"Your Passwords did not match")   
            return redirect('/signup/')    
    else:           
        return render(request,'signup.html')
    
def Login(request):
        if request.method=='POST':
            uname=request.POST.get('uname')
            pas=request.POST.get('password')
            user=authenticate(username=uname,password=pas) 
            if user is not None:
                login(request,user)
                us=User.objects.get(username=uname)
                return redirect('/secure/{}'.format(us))
            else:
                messages.error(request,"Invalid Username or Password",extra_tags='danger')
                return redirect('/Login/') 
        else:       
            return render(request,'login.html')
        
def secure(request,id):
    if request.user.is_authenticated :
        s=Schedule.objects.raw('select accounts_schedule.*,accounts_doctor.* from accounts_schedule,accounts_doctor where accounts_schedule.doctor_id=accounts_doctor.did')
        
        return render(request,'secure.html',{'sc':s,'id':id})
    else:
        return redirect('/Login/')
    
def Logout(request):
    if request.user.is_authenticated :
        logout(request)
        return render(request,'login.html')
    
def app(request,did,id):
    if request.method=='POST':
         date=request.POST.get('date')
         d=Doctor.objects.get(did=did)
         us=User.objects.get(username=id)
         t=Appointment(doctor=d, user=us,appdate=date)
         t.save()
         if(t is not None):
             messages.success(request,'Your Appointment is booked with {}. We will send you the confirmation mail with the time in few minutes.'.format(d.dname))
             return render(request,'app.html')
         else:
             messages.error(request,'Appointment fail, Please try again.')
             return render(request,'app.html')
    else:
         return render(request,'app.html')
 

             