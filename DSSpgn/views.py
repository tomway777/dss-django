from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
from DSSpgn.processing import process

def front(request):
    # post = dc.objects.using('pgn').latest('id').flow
    # print(post)
    sur = process()
    surv = sur.calculateSVT()
    print(surv)
    return render(request, 'template/dashboard/front.html')

def dashboard(request):
    return  render(request, 'template/dashboard/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun telah terbuat untuk {username}')
            return redirect('/login/')
    else:
        form = UserRegistrationForm()
    return render(request,'template/registration/register.html', {'form' :form})

def login(request):
    return render(request, 'template/registration/login.html')