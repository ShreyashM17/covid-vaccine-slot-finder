from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm, PasswordForm, Login
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
import uuid
from .models import Registrations
from datetime import date
import requests
import math
import random
from . import encoder


# Create your views here.
def homepage(request):
    User = request.user
    User = str(User)
    print(User)
    user_reg1 = Registrations.objects.all().filter(device1=User)
    user_reg2 = Registrations.objects.all().filter(device2=User)
    user_reg3 = Registrations.objects.all().filter(device3=User)
    if (len(user_reg1) or len(user_reg2) or len(user_reg3)) != 0:
        details = None
        if len(user_reg1) != 0:
            details = Registrations.objects.get(device1=User)
        elif len(user_reg2) != 0:
            details = Registrations.objects.get(device2=User)
        elif len(user_reg3) != 0:
            details = Registrations.objects.get(device3=User)
        email_id = details.Email_id
        return redirect(f'slotfinder/{email_id}')
    return redirect('login/')


def login(request):
    form = Login(request.POST or None)
    incorrect = False
    if request.method == 'POST':
        if form.is_valid():
            email_id = form.cleaned_data['Email_id']
            password1 = form.cleaned_data['Password']
            datana = Registrations.objects.all().filter(Email_id=email_id)
            if len(datana) == 0:
                return HttpResponse("Not Registered")
            else:
                data = Registrations.objects.get(Email_id=email_id)
                if data.Verified:
                    passworden = data.Password
                    passwordact = encoder.decoder(passworden)
                    if passwordact == password1:
                        device = str(request.user)
                        device1 = data.device1
                        device2 = data.device2
                        device3 = data.device3
                        if device1 is None:
                            data.device1 = device
                        elif device2 is None:
                            data.device2 = device
                        elif device3 is None:
                            data.device3 = device
                        else:
                            return HttpResponse("Maximum device limit has reached log out from previous devices to continue login")
                        data.save()
                        return redirect(f'http://127.0.0.1:8000/slotfinder/{email_id}')
                    else:
                        incorrect = True
                else:
                    return HttpResponse("Not Registered")
    context = {
        'form': form,
        'incorrect': incorrect
    }
    return render(request, 'login.html', context)


def signup(request):
    form = SignupForm(request.POST or None)
    sent = False
    if request.method == 'POST':
        if form.is_valid():
            data = form.clean_data()
            email_id = data['email_id']
            f_name = data['first_name']
            l_name = data['last_name']
            phone_number = data['phone_number']
            dob = data['dob']
            document = data['document'],
            doc_no = data['doc_no']
            uid = generate_uid()
            new_user = Registrations(Uid=uid, Email_id=email_id, First_name=f_name, Last_name=l_name,
                                     Phone_number=phone_number
                                     , Date_of_birth=dob, Document=document, document_no=doc_no)
            new_user.save()
            template = get_template('emailtemplate.html').render({'uid': uid})
            email = EmailMessage(
                'subject',
                template,
                settings.EMAIL_HOST_USER,
                [request.POST.get('Email_id')],
            )
            email.content_subtype = 'html'
            email.fail_silently = False
            email.send()
            sent = True
    context = {
        'form': form,
        'sent': sent,
    }
    return render(request, 'signup.html', context)


def verified(request, uid):
    found = Registrations.objects.all().filter(Uid=uid)
    if len(found) == 0:
        return HttpResponse("Already Verified or not registerd")
    else:
        user_detail = Registrations.objects.get(Uid=uid)
        user_detail.Verified = True
        user_detail.save()
    return redirect(f'password/{uid}')


def password(request, uid):
    form = PasswordForm(request.POST or None)
    notmatch = False
    found = Registrations.objects.all().filter(Uid=uid)
    Name = ""
    if len(found) == 0:
        return HttpResponse("Already Verified or not registerd")
    else:
        if request.method == 'POST':
            if form.is_valid():
                user_detail = Registrations.objects.get(Uid=uid)
                Name= user_detail.First_name
                passwordnew = request.POST.get('newpassword')
                passwordre = form.cleaned_data['Password']
                if passwordre == passwordnew:
                    passworden = encoder.encoder(passwordre)
                    user_detail.Password = passworden
                    uid = generate_uid()
                    user_detail.Uid = uid
                    user_detail.save()
                    return redirect('login')
                else:
                    notmatch = True
    context = {
        'Password': PasswordForm,
        'name': Name,
        'notmatch': notmatch
    }
    return render(request, 'Newpassword.html', context)


def locator(request, email_id):
    detail = Registrations.objects.get(Email_id=email_id)
    uid = detail.Uid
    context = {
        'uid': uid,
        'email_id': email_id
    }
    return render(request, 'locator.html', context)


def slot(request, email_id):
    detail = Registrations.objects.get(Email_id=email_id)
    uid = detail.Uid
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    pin_in = request.GET.get('pincode')
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={a}&date={b}'.format(a=pin_in,
                                                                                                               b=today)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/90.0.4430.93 Safari/537.36)'}
    result = requests.get(url, headers=header)
    result = result.json()
    print(result)
    i = 0
    data = []
    for j in result['sessions']:
        info = ["Centre name: " + str(result['sessions'][i]['name']),
                "Minimum age limit: " + str(result['sessions'][i]['min_age_limit']),
                "Available Capacity:" + str(result['sessions'][i]['available_capacity']),
                "Fee type:" + str(result['sessions'][i]['fee_type']),
                "Address: " + str(result['sessions'][i]['address'])]
        data.append(info)
        i = i + 1
    context = {
        'slots': data,
        'uid': uid
    }
    return render(request, 'slots.html', context)


def resetpass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        find = Registrations.objects.all().filter(Email_id=email)
        if len(find) == 0:
            return HttpResponse("Email not found")
        else:
            user_details = Registrations.objects.get(Email_id=email)
            uid = user_details.Uid
            user_details.Password = None
            user_details.save()
            template = get_template('emailtemplate.html').render({'uid': uid})
            email = EmailMessage(
                'subject',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.content_subtype = 'html'
            email.fail_silently = False
            email.send()
            return HttpResponse("Email sent successfully")
    return render(request, 'resetpassword.html')


def logout(request,uid):
    data = Registrations.objects.get(Uid=uid)
    current_user = str(request.user)
    device1 = data.device1
    device2 = data.device2
    device3 = data.device3
    if current_user == device1:
        data.device1 = None
    elif current_user == device2:
        data.device2 = None
    elif current_user == device3:
        data.device3 = None
    data.save()
    return redirect('/')


def generate_uid():
    while True:
        uid = str(uuid.uuid4())[:20]
        value = Registrations.objects.all().filter(Uid=uid)
        if len(value) == 0:
            break
    return uid
