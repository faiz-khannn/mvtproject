from django.shortcuts import redirect, render
from django.http import HttpResponse
from mvtapp.models import Tb
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
  # print('hello')
  # return HttpResponse('Hello') 
  return render(request, 'home.html')

@login_required
def about(request):
  return render (request,'about.html')

@login_required
def data(request):
  emp = Tb.objects.all()
  Tblist = []
  for e in emp:
    d = e.__dict__
    del(d['_state'])
    Tblist.append(d)
  return render(request, 'data.html',{'emp':Tblist})

@login_required
@csrf_exempt
def insert(request):
  if request.method == 'POST':
    id = request.POST['ID']
    name = request.POST['Name']
    Branch = request.POST['Branch']
    dob = request.POST['DOB']
    cn = request.POST['contactNo']
    ad = request.POST['address']
    objemp = Tb(id,name,Branch,dob,cn,ad)
    objemp.save()
    return render(request,'insert.html')

    
  return render(request,'insert.html')
  
def delete(request,id):
  emp = Tb.objects.get(empid=id)
  emp.delete()
  return redirect('/data')
 
@csrf_exempt
def update(request,id):
  if request.method == 'POST':
    id = request.POST['ID']
    name = request.POST['Name']
    Branch = request.POST['Branch']
    dob = request.POST['DOB']
    cn = request.POST['contactNo']
    ad = request.POST['address']
    obj = Tb.objects.filter(empid=id).update(empid=id, empname=name, branch=Branch, empdob=dob, contactno=cn, address=ad)
    return redirect('/data')
  
  obj = Tb.objects.get(empid=id)
  data = (obj.__dict__)
  del(data['_state'])
  return render(request,'update.html', {'data':data})

def signin(request):
  if request.method=='POST':
    username=request.POST.get('username')
    pass1=request.POST.get('pass')
    user=authenticate(request,username=username,password=pass1)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      return HttpResponse ("Username or Password is incorrect!!!")
  return render(request, 'login.html')
  
  
def register(request):
  if request.method=='POST':
    uname=request.POST.get('username')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')

    if pass1!=pass2:
      return HttpResponse("Your Passwords dose'nt match!!!")
    else:
      my_user=User.objects.create_user(uname,email,pass1)
      my_user.save()
    return redirect('login')
  return render (request,'register.html')

def logoutp(request):
    logout(request)
    return redirect('login')
