from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
from DSSpgn.processing import process

def front(request):
    # post = dc.objects.using('pgn').latest('id').flow
    # print(post)
    #TODO: Cek session dan ambil user yg masuk
    sur = process()
    # surv = sur.getJarakMs('Jes','MRU Gresik')
    surv = sur.getGTMStanby(ms=2)
    print(surv)
    return render(request, 'template/dashboard/front.html')
#--------------------------------------------------------------------#
proc = process() #objek class processing
def dashboard(request):
    idprs = 1
    namams = proc.getNamaMS(ms_id=1)
    prs = proc.getDataPRS()
    temp = {}
    listnew = []
    for i in prs:
        svt = proc.calculateSVT(i['flow'],i['pressureoutlet'],5)
        temp['survivaltime'] = svt
        tempdict = {**i, **temp}
        listnew.append(tempdict)
    print(listnew)
    #getcurrgtm --- percobaan pake id ms 2
    currgtm = proc.getGTMStanby(ms=2)
    contex = {'namams' : namams, 'listprs' : listnew, 'currgtm' : currgtm}
    return  render(request, 'template/dashboard/dashboard.html', contex)



#------------------------------------------------------------------------#
def dashboardpwkt(request):
    idprs = 2
    namams = proc.getNamaMS(ms_id=2)
    context = {'namams' : namams}
    return render(request,'template/dashboard/dashboardpwkt.html', context)

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