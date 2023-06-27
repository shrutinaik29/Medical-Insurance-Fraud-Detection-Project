from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import MyModel
import csv
from django.contrib.auth import authenticate, login, logout

def home(request):
    context={}
    return render(request, "myApp/home.html",context)

def signuppage(request):
     form=CreateUserForm()

     if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('login')
     else:
        context= {'form':form}
     return render(request,"myApp/signup.html", context)
    #if request.method=='POST':
        #uname=request.POST.get('Your Name')
        #email=request.POST.get('Your Email')
        #password=request.POST.get('Password')
       # password2=request.POST.get('Repeat your password')
        #if password==password2:
          # my_user=User.objects.create_user(uname,email,password)
          # my_user.save()
          # print('user created')
       # else:
           # print('password not matching')

        #print(uname,email,password,password2)#
    
def search_data(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        try:
            obj = MyModel.objects.get(field1=search_query)
        except MyModel.DoesNotExist:
            return HttpResponse('Data not found. Fraudulent.')

        with open('C:\\Users\\SUNIL\\OneDrive\\Desktop\\djnagoprj\\myProject\\myApp\\__pycache__\\data\\medical_aid_claims.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['member_name'] == search_query:
                    return render(request, 'search_result.html', {'data_found': True})

        return render(request, 'search_result.html', {'data_found': False})


    return HttpResponse('Invalid request.')

def loginpage(request):

    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
        
       user = authenticate(request, username=username, password=password)

       if user is not None:
          login(request,user)
          return redirect('home')
       else:
          messages.info(request, 'Username OR Password is incorrect/././.....!!!')
          return render(request,"myApp/login.html")

    context ={}
    return render(request,"myApp/login.html")

def logoutUser(request):
    return redirect('login')

def application(request):
    return render(request,'myApp/application.html')

def feedbach(request):
    return render(request,'myApp/feedbach.html')

def enter_name_amount(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        
        # Process the data as needed, e.g., save it to the database
        
        return render(request, 'search_result.html')  # Render the success template

    return render(request, 'application.html')  # Render the form template
