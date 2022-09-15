from django.shortcuts import render, redirect
from django.http import request,HttpResponseRedirect,HttpResponse
from .models import LoginForm, VerifyDocument,feedback
from .forms import LoginField, VerifyDocumentForm, RegistrationForm, feedbackForm
import qrcode
import os
from digita.settings import BASE_DIR
from django.contrib import messages
import uuid
# Create your views here.

def index(request):
      if 'user' in request.session:
            print("Hello")
            user = LoginForm.objects.get(email=request.session['user'])
            print(user)
            if request.POST:
                  name= request.POST['name']
                  email = request.POST['email']
                  message = request.POST['message'] 

                  obj = feedback()
                  obj.name = name
                  obj.email = email
                  obj.message = message
                  obj.save()
                  return redirect('index')
            else:
                  return render(request,'index.html',{'user':user.username}) 
            return render(request,'index.html')
      else:
            return redirect('login')

def logout(request):
  if request.session.keys():
        del request.session['user']
        return redirect('login')
        
def log(request):
  if request.method=="POST":
        try:
            m = LoginForm.objects.get(username=request.POST['username'])
            if m.password == request.POST['password']:
                request.session['user'] = m.email
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password </a></h2>")
        except:
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
  return render(request, 'log1.html')


def verifyDoc(request):
      if 'user' in request.session:
            user = LoginForm.objects.get(email=request.session['user'])
            if request.method=="POST":
                  try:
                        print(request.session['user'])
                        user = LoginForm.objects.get(email=request.session['user'])
                        m = VerifyDocument.objects.get(user_data=user,doc_no=request.POST['doc_no'])
                        print(m.doc_name)
                        print(m.doc_no)
                        if m.doc_name == request.POST['doc_name']:
                              print("dd")
                              if m.qrcode != '':
                                    return HttpResponse("<h2><a href=''>already verified</a></h2>")
                              name = user.username+"_"+m.doc_name
                              data = "User Name = "+user.username+"\nDocument name = "+m.doc_name+"\nDocument No = "+str(m.doc_no)
                              qr=qrcode.QRCode(version=1,box_size=10,border=5)
                              qr.add_data(data)
                              print("ee")
                              qr.make(fit=True)
                              img=qr.make_image(fill="black",back_color="white")
                              img.save(os.path.join(BASE_DIR,"media/"+ name +".jpeg"))
                              m.qrcode = name +".jpeg"
                              m.save()

                              return render(request,'document_very1.html',{'m':m,'user':user.username})
                        else:
                              return HttpResponse("<h2><a href=''>You have entered wrong details </a></h2>")
                  except:
                        return redirect('error')
            return render(request, 'document_very.html',{'user':user})
      else:
            return redirect('login')

def verifiedDocument(request):
      if 'user' in request.session:
            user = LoginForm.objects.get(email=request.session['user'])
            data = VerifyDocument.objects.filter(user_data=user)
            print(data)
            li = []
            for i in data:
                  if i.qrcode != '':
                        print(i)
                        li.append(i)
            return render(request,'verified_doc.html',{'li':li, 'user':user})   
      else:
            return redirect('login')      
            
def registration(request):
  if request.POST:
    username = request.POST['username']
    email = request.POST['email']
    mobile = request.POST['mobile']
    gender = request.POST['gender']
    dddd = request.POST['birthday']
    password = request.POST['password']
    conf_pass = request.POST['conf_password']
    hint = request.POST['hint']

    obj = LoginForm()
    obj.username = username
    obj.dob = dddd
    obj.gender = gender
    obj.email = email 
    obj.mobile = mobile
    obj.password = password
    obj.confirm_password = conf_pass
    obj.hint = hint
    
    obj.save()
    return redirect('index')
  else:
    return render(request,'registeration1.html')

def Feedback(request):
      if request.POST:
            name= request.POST['name']
            email = request.POST['email']
            message = request.POST['message'] 
            obj = feedback()
            obj.name = name
            obj.email = email
            obj.message = message
            obj.save()
            return redirect('index')
      else:
            return render(request,'index.html') 

def card(request):
      if 'user' in request.session:
            user = LoginForm.objects.get(email=request.session['user'])
            m=user.unique
            if user.status ==True:
                  return render(request,'card.html',{'m':m,'user':user})
            else:
                  return redirect('error')        
               
      else:
            return redirect('login') 

def errorpage(request):
      return render(request,'error.html')

def confirm(request):
      if request.method == 'POST':
            try:
                  model = LoginForm.objects.get(username = request.POST['username'])
                  if model.hint == request.POST['hint']:
                        request.session['forgot'] = model.username
                        return redirect('forgotpassword')
                  else:
                        return HttpResponse("<a href = ''>Your Hint is Wrong</a>")
            except:
                  return HttpResponse("<a href = ''>Please Enter Correct Username</a>")
      return render(request,'confirm.html')

def forgotpassword(request):
      if request.method == 'POST':
            try:
                  username = request.session['forgot']
                  model = LoginForm.objects.get(username = username)
                  password = request.POST['password']
                  conf_password = request.POST['password1']
                  model.password = password
                  model.confirm_password = conf_password
                  model.save()
                  return redirect('login')
            except:
                  return HttpResponse("<a href = ''>Something Went Wrong</a>")
      return render(request,'forgot-password.html')