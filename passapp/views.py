from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import Login
from django.contrib.auth.hashers import make_password, check_password

def login(request, decryptedpassword):
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)
        print(decryptedpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'index.html')