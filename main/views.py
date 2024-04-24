from django.shortcuts import render,redirect
from PIL import Image
import pytesseract
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
from django.contrib.auth.decorators import login_required



def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username=None
            email=None
            password=None
            passwordconfigration=None
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            passwordconfigration=request.POST['passwordconfigration']
            # user = None
            if User.objects.filter(email=email).exists():
                pass
            else:
                if password != passwordconfigration:
                    pass
                else:
                    user = User.objects.create_user(
                    username=username,
                    is_active=True,
                    email=email,
                    password=password,
                    )
                    user.save()
            # if user is not None:
            #     login(request, user)
                return redirect('/login')
        return render(request,'register.html')
    

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
        return render(request,'login.html')
from django.http import JsonResponse

@login_required(login_url='/login/')
def extractt(request):
        
    return render(request,'main.html')

def extract(request):
    text = ''
    if request.method == 'POST':
        if 'img' in request.FILES:
            img = request.FILES['img']
        image = Image.open(img)
        configg=f'--psm 6 --oem 3'
        text = pytesseract.image_to_string(image,lang='chi_tra +chi_sim',config=configg)
    return JsonResponse({'text': text})
