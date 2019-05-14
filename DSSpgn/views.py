from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
from DSSpgn.processing import process
from DSSpgn.olah import olah

# def sarangtm(request, idgtm):
#     return HttpResponse('<h1>This is it {}. </h1>'.format(idgtm))

def getidgtm(request,id):
    name = id
    sur = process()
    data = sur.getIdbyName(name)
    allprs = sur.getAllprs_nonsol()
    # print(allprs)
    solusi = sur.showcater_prs(1, name)
    context = {'id' : name, 'data': data, 'allprs' : allprs, 'solusi' : solusi}

    return render(request, 'template/dashboard/sarantujuan.html', context)

def getidgtmjes(request,id):
    name = id
    sur = process()
    data = sur.getIdbyName(name)
    allprs = sur.getAllprs_nonsol()
    # print(allprs)
    context = {'id' : name, 'data': data, 'allprs' : allprs}
    tes = sur.showcater_prs(3,name)
    return render(request, 'template/dashboard/sarantujuanjes.html', context)

def getidgtmindo(request,id):
    name = id
    sur = process()
    data = sur.getIdbyName(name)
    allprs = sur.getAllprs_nonsol()
    # print(allprs)
    context = {'id' : name, 'data': data, 'allprs' : allprs}
    tes = sur.showcater_prs(4,name)
    return render(request, 'template/dashboard/sarantujuanindogas.html', context)

def getidgtmpur(request,id):
    name = id
    sur = process()
    data = sur.getIdbyName(name)
    allprs = sur.getAllprs_nonsol()
    # print(allprs)
    context = {'id' : name, 'data': data, 'allprs' : allprs}
    tes = sur.showcater_prs(2,name)
    return render(request, 'template/dashboard/sarantujuanpur.html', context)



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

    # ol = olah()
    # ol.getData(msid=1)
    idms = 1
    namams = proc.getNamaMS(ms_id=idms)
    # jarak = proc.getJarakMs(ms=idms,prs=1)
    # print(jarak)
    prs = proc.getDataPRS()
    # print(prs)
    temp = {}
    listnew = []
    for i in prs:
        svt = proc.calculateSVT(i['flow'],i['pressureoutlet'], i['conkap'])
        temp['survivaltime'] = svt
        tempdict = {**i, **temp}
        listnew.append(tempdict)
    # print(listnew)
    #getcurrgtm --- percobaan pake id ms 2
    currgtm = proc.getGTMStanby(ms=idms)
    contex = {'namams' : namams, 'listprs' : listnew, 'currgtm' : currgtm}
    return  render(request, 'template/dashboard/dashboard.html', contex)



#------------------------------------------------------------------------#
def dashboardpwkt(request):
    idms = 2
    namams = proc.getNamaMS(ms_id=idms)
    prs = proc.getDataPRS()
    temp = {}
    listnew = []
    for i in prs:
        svt = proc.calculateSVT(i['flow'],i['pressureoutlet'],i['conkap'])
        temp['survivaltime'] = svt
        tempdict = {**i, **temp}
        listnew.append(tempdict)
    print(listnew)
    #getcurrgtm --- percobaan pake id ms 2
    currgtm = proc.getGTMStanby(ms=idms)
    contex = {'namams' : namams, 'listprs' : listnew, 'currgtm' : currgtm}
    return render(request,'template/dashboard/dashboardpwkt.html', contex)
#------------------------------------------------------------------------#
def dashboardjes(request):
    idms = 3
    namams = proc.getNamaMS(ms_id=idms)
    prs = proc.getDataPRS()
    temp = {}
    listnew = []
    for i in prs:
        svt = proc.calculateSVT(i['flow'],i['pressureoutlet'], i['conkap'])
        temp['survivaltime'] = svt
        tempdict = {**i, **temp}
        listnew.append(tempdict)
    print(listnew)
    #getcurrgtm --- percobaan pake id ms 2
    currgtm = proc.getGTMStanby(ms=idms)
    contex = {'namams' : namams, 'listprs' : listnew, 'currgtm' : currgtm}
    return render(request,'template/dashboard/dashboardjes.html', contex)
#------------------------------------------------------------------------#
def dashboardindogas(request):
    idms = 4
    namams = proc.getNamaMS(ms_id=idms)
    prs = proc.getDataPRS()
    temp = {}
    listnew = []
    for i in prs:
        svt = proc.calculateSVT(i['flow'],i['pressureoutlet'], i['conkap'])
        temp['survivaltime'] = svt
        tempdict = {**i, **temp}
        listnew.append(tempdict)
    print(listnew)
    #getcurrgtm --- percobaan pake id ms 2
    currgtm = proc.getGTMStanby(ms=idms)
    contex = {'namams' : namams, 'listprs' : listnew, 'currgtm' : currgtm}
    return render(request,'template/dashboard/dashboardindogas.html', contex)

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