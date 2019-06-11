from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
# Create your views here.
from DSSpgn.processingnew import processingnew
from django.contrib.auth.decorators import login_required

def front(request):
    return render(request, 'template/dashboard/front.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun telah terbuat untuk {username}')
            # request.session['username'] = username
            return redirect('/login/')
    else:
        form = UserRegistrationForm()
    return render(request,'template/registration/register.html', {'form' :form})

# def login(request):
#     # print(request.GET.get('username'))
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 request.session.set_expiry(86400)
#                 login(request,user)
#         else:
#             return redirect('/login/')

def login(request):
    return render(request, 'template/registration/login.html')
    # username = 'not logged in'
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         request.session['username'] = username
    #     else:
    #         form = LoginForm()
    # return render(request, 'template/registration/login.html', {"username" : username})

@login_required
def GTM(request):
    pros = processingnew()
    s = pros.getGtmstandby()
    context = {'gtm' : s}
    return render(request, 'template/dashboard/GTM.html', context)

@login_required
def PRS(request):
    # if request.session.has_key('username'):
    # username = request.session['username']
    pros = processingnew()
    s = pros.getDataPrs()
    contex = {'surv': s}
    return render(request, 'template/dashboard/PRS.html',contex)
    # else:
    #     return redirect('/login/')

@login_required
def getidgtm(request,id):
    ms = 2
    name = id
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuan.html', context)

@login_required
def getidgtmjes(request,id):
    name = id
    ms = 3
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuanjes.html', context)

@login_required
def getidgtmindo(request,id):
    name = id
    ms = 4
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuanindogas.html', context)

@login_required
def getidgtmpur(request,id):
    name = id
    ms = 1
    pros = processingnew()
    sol = pros.showSaran(ms,name)
    alt = pros.getAltsolusi(sol)

    context = {'saran' : sol[0][0], 'alt' : alt}
    return render(request, 'template/dashboard/sarantujuanpur.html', context)


#

#--------------------------------------------------------------------#
@login_required
def dashboard(request):
    ms = 2
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm' : gtm}
    return  render(request, 'template/dashboard/dashboard.html', context)
#------------------------------------------------------------------------#
@login_required
def dashboardpwkt(request):
    ms = 1
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm' : gtm}
    return render(request,'template/dashboard/dashboardpwkt.html', context)
#------------------------------------------------------------------------#
@login_required
def dashboardjes(request):
    ms = 3
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm': gtm}
    return render(request,'template/dashboard/dashboardjes.html', context)
#------------------------------------------------------------------------#
@login_required
def dashboardindogas(request):
    ms = 4
    pros = processingnew()
    gtm = pros.getGTMstanby(ms=ms)
    context = {'gtm': gtm}
    return render(request,'template/dashboard/dashboardindogas.html', context)
#------------------------------------------------------------------------#
