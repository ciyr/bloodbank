from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from .models import Region, Donor, Receiver
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def home(request):
    return render(request, 'home.html')

# def login(request):
    
#     return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('bloodmatch:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def register_donor(request):
    if request.method == 'POST':
        try:
            user=request.user
            email= request.POST['email']
            name = request.POST['name']
            age = request.POST['age']
            aadhar_no = request.POST['aadhar_no']
            blood_group = request.POST['blood_group']
            phone_number = request.POST['phone_number']
            address = request.POST['address']
            hemoglobin = request.POST['hemoglobin']
            city = request.POST['city']
            region = Region.objects.get(city=city)  
            state= region.state          
            donor = Donor(user=user, name=name,email=email, age=age, aadhar_no=aadhar_no, blood_group=blood_group, phone_number=phone_number, address=address, hemoglobin=hemoglobin, city=region)
            donor.save()
            try:
                receiver = Receiver.objects.get( blood_group=blood_group, city__state=state)
                if receiver:
                    rmail = receiver.email
                    rname = receiver.name
                    mailtemp = f"Dear {rname},\n\nWe have found a match for your {blood_group} blood group.\nPlease contact {email} living in {address}, {city} regarding the same. \n\nRegards,\nBloodbank Team"
                    subject = "Blood Match"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [rmail]
                    send_mail(subject, mailtemp, email_from, recipient_list)
                    donor.delete()
                    receiver.delete()
            except Receiver.DoesNotExist:
                pass
            return redirect('bloodmatch:home')
        except IntegrityError:
            #  return redirect('bloodmatch:register_donor')
            # return render_to_response("template.html", {"message": e.message})
            return render(request, 'donate_blood.html', {'message': 'You have already registered as a donor.'})
    

    return render(request, 'donate_blood.html')

@login_required
def register_receiver(request):
    if request.method == 'POST':
        try:
            user=request.user
            name =request.POST['name']
            email= request.POST['email']
            age = request.POST['age']
            aadhar_no = request.POST['aadhar_no']
            blood_group = request.POST['blood_group']
            phone_number = request.POST['phone_number']
            address = request.POST['address']
            city = request.POST['city']
            region = Region.objects.get(city=city)
            state= region.state
            receiver = Receiver(user=user,name=name, email=email,age=age, aadhar_no=aadhar_no, blood_group=blood_group, phone_number=phone_number, address=address, city=region)
            receiver.save()
            try:
                donor = Donor.objects.get( blood_group=blood_group, city__state=state)
                if donor:
                    dmail = donor.email
                    daddress= donor.address
                    dcity=donor.city
                    mailtemp = f"Dear {name},\n\nWe have found a match for your {blood_group} blood group.\nPlease contact {dmail} living in {daddress}, {dcity} regarding the same. \n\nRegards,\nBloodbank Team"
                    subject = "Blood Match"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    send_mail(subject, mailtemp, email_from, recipient_list)
                    donor.delete()
                    receiver.delete()
            except Donor.DoesNotExist:
                pass                
            return redirect('bloodmatch:home')
        except IntegrityError:
            return render (request, 'request_blood.html', {'message': 'You have already registered as a receiver. Kindly signup as a new user.'})

    return render(request, 'request_blood.html')



