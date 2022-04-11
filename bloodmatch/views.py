from django.shortcuts import render
from .models import Region, Donor, Receiver
#import login required decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'bloodmatch/templates/home.html')

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
        return render(request, 'bloodmatch/templates/home.html')

    return render(request, 'bloodmatch/templates/request_blood.html')

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
        return render(request, 'bloodmatch/templates/home.html')

    return render(request, 'bloodmatch/templates/request_blood.html')

