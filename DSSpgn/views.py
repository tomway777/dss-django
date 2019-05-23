from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
from DSSpgn.processing import process
from DSSpgn.processingnew import processingnew


def GTM(request):
    pros = processingnew()
    s = pros.getGtmstandby()
    context = {'gtm' : s}
    return render(request, 'template/dashboard/GTM.html', context)

def PRS(request):
    pros = processingnew()
    s = pros.getDataPrs()
    contex = {'surv': s}
    return render(request, 'template/dashboard/PRS.html',contex)


def getidgtm(request,id):
    ms = 2
    name = id
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuan.html', context)

def getidgtmjes(request,id):
    name = id
    ms = 3
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuanjes.html', context)

def getidgtmindo(request,id):
    name = id
    ms = 4
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuanindogas.html', context)

def getidgtmpur(request,id):
    name = id
    ms = 1
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuanpur.html', context)


#
def front(request):
    return render(request, 'template/dashboard/front.html')
#--------------------------------------------------------------------#

def dashboard(request):
    ms = 2
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm' : gtm}
    return  render(request, 'template/dashboard/dashboard.html', context)
#------------------------------------------------------------------------#
def dashboardpwkt(request):
    ms = 1
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm' : gtm}
    return render(request,'template/dashboard/dashboardpwkt.html', context)
#------------------------------------------------------------------------#
def dashboardjes(request):
    ms = 3
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm': gtm}
    return render(request,'template/dashboard/dashboardjes.html', context)
#------------------------------------------------------------------------#
def dashboardindogas(request):
    ms = 4
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm': gtm}
    return render(request,'template/dashboard/dashboardindogas.html', context)
#------------------------------------------------------------------------#
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