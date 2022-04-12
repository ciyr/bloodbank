from django.shortcuts import render
from .models import Region, Donor, Receiver

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate

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
        name = request.POST['name']
        age = request.POST['age']
        aadhar_no = request.POST['aadhar_no']
        blood_group = request.POST['blood_group']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        hemoglobin = request.POST['hemoglobin']
        city = request.POST['city']
        region = Region.objects.get(city=city)
        donor = Donor(name=name, age=age, aadhar_no=aadhar_no, blood_group=blood_group, phone_number=phone_number, address=address, hemoglobin=hemoglobin, city=region)
        donor.save()
        return render(request, 'home.html')

    return render(request, 'donate_blood.html')

@login_required
def register_receiver(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        aadhar_no = request.POST['aadhar_no']
        blood_group = request.POST['blood_group']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        region = Region.objects.get(city=city)
        receiver = Receiver(name=name, age=age, aadhar_no=aadhar_no, blood_group=blood_group, phone_number=phone_number, address=address, city=region)
        receiver.save()
        return render(request, 'home.html')

    return render(request, 'request_blood.html')




