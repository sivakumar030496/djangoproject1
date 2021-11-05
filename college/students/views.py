from django.db.models import *
from django.shortcuts import render,redirect
from .models import Studentdata
from .forms import StudentsForm
from django.contrib.auth import authenticate,logout,login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    return render(request,'home.html')

def index(request):
    college=Studentdata.objects.all
    return render(request,'index.html',{'college':college})

def create(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/index/')
    form = StudentsForm()
    return render(request,'create.html',{'form':form})

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('password1')
        if password==confirmpassword:
            user= User. objects.create_superuser(username=username,email=email,password=password)
        user.save()
        send_mail('login link',
                  'User registered Successfully'
                  'http"//127.0.0.1:8000/students/login/',
                  settings.EMAIL_HOST_USER,
                  [email])
        return redirect('/students/login/')
    else:
        print('enter valid password')
    return render(request,'register.html')

def edit(request, id):
    student_data = Studentdata.objects.get(id = id)
    form = StudentsForm(instance=student_data)
    return render(request, 'update.html',{'form':form, 'id':id})

def update(request, id):
    student_data=Studentdata.objects.get(id=id)
    form=StudentsForm(request.POST, instance=student_data)
    if form.is_valid():
        form.save()
        return redirect('/students/index/')
    return render(request, 'update.html',{'form':form})

def delete(request, id):
    student_data=Studentdata.objects.get(id=id)
    student_data.delete()
    return redirect('/students/index/')

def us_login(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('/students/index/')
    return render(request,'login.html',{})

def us_logout(request):
    logout(request)
    return redirect('/students/login/')

def queriesql(request):
    COUNT=Studentdata.objects.all().count()
    AVERAGE=Studentdata.objects.aggregate(Avg('Markspersentage'))
    AVG=AVERAGE['Markspersentage__avg']
    MINIMUM=Studentdata.objects.aggregate(Min('Markspersentage'))
    MIN=MINIMUM['Markspersentage__min']
    MAXIMUM=Studentdata.objects.aggregate(Max('Markspersentage'))
    MAX=MAXIMUM['Markspersentage__max']
    GREATER=Studentdata.objects.filter(Markspersentage__gte=70).count()
    FAIL=Studentdata.objects.filter(Markspersentage__lt=40).count()
    s=[COUNT,AVG,MIN,MAX,GREATER,FAIL]
    z=['COUNT','AVERAGE','MINIMUM','MAXIMUM','GREATER','FAIL']
    return render(request,'queries.html',{'z':z,'s':s})


