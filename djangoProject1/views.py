from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Formdan gelen verileri kullanarak yeni bir User nesnesi oluştur
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            new_user.phone_number = form.cleaned_data['phone_number']  # Ekstra alanları da atayabilirsin
            new_user.save()  # Kullanıcıyı veritabanına kaydet
            return redirect('login')  # Başarılı kayıt olduktan sonra login sayfasına yönlendir
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

