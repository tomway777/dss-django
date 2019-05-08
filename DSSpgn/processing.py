from DSSpgn.models_pgn import Datacater,Masterprs, Mastergtm, Mastermotherstation, Datagtm, Masterstatus, Detaildatams
from DSSpgn.models import Datadetailprs, post_record

class process():
    # def calculateSVT(self):
    # #TODO: cek kalkulasi sruvival time
    #     flow = Datacater.objects.using('pgn').latest('id').flow
    #     pressure = Datacater.objects.using('pgn').latest('id').pressureoutlet
    #     capacity = 5
    #     calc =  (pressure * capacity) / flow
    #     return calc

    def calculateSVT(self, flow, pressure, capacity):
    #TODO: Kalkulasi surv time
        calc =  (pressure * capacity) / flow
        return calc
    #--------------------------------Ambil Nama----------------------------------------------#
    def getNamaMS(self, ms_id=None):
        nama = Mastermotherstation.objects.using('pgn').get(id=ms_id).namams
        return nama

    def getPrsName(self, idPrs=None):
        nama = Masterprs.objects.using('pgn').get(id=idPrs).namaprs
        return nama
    # ---------------------------------Ambil Data flow & preassure-----------------------------------------#
    def getDataPRS(self):
        listnama = {}
        listbaru = []
        prs = Datacater.objects.using('pgn').all().order_by('waktu').values('idprs','flow','pressureoutlet')
        listdict = list(prs)
        for i in listdict:
            for k,v in i.items():
                if k == 'idprs':
                    listnama['namaprs'] = self.getPrsName(v)
                    templist = {**i, **listnama}
                    listbaru.append(templist)
                    # listnama.append(self.getPrsName(v))
        return listbaru

    # -----------------------------------Ambil Jarak & sesuai MS & PRS------------------------------------#

    def getJarakMs(self, ms=None, prs=None):
        data = Detaildatams.objects.using('pgn').get(iddatams=ms, idprs=prs).jarak
        calculate = data/20
        return calculate

    # ----------------------------------Ambil GTM Standby--------------------------------------------#
    def getGTMStanby(self, ms=None):
        tempdict = {}
        comdict = {}
        listbaru = []
        currGTM = Datagtm.objects.using('pgn').filter(status=1, idms=ms) #ambil status gtm standby di ms
        listgtm = list(currGTM.values())
        for i in listgtm:
           for k,v in i.items():
               if k == 'idgtm': #ambil nama gtm dan kapasitas gtm
                    namagtm = Mastergtm.objects.using('pgn').get(id=v).nogtm
                    kapasitas = Mastergtm.objects.using('pgn').get(id=v).kapasitasgtm
                    tempdict['NoGtm'] = namagtm
                    tempdict['Kap'] = kapasitas
                    comdict = {**i, **tempdict}
               elif k == 'status':
                    namastatus = Masterstatus.objects.using('pgn').get(id=v).namastatus
                    tempdict['status'] = namastatus
                    comdict = {**comdict, **tempdict}
                    listbaru.append(comdict)
        return listbaru
    #--------------------------------------------------------------------------------------------------#
    def getIdbyName(self, name):
        datagtm = Mastergtm.objects.using('pgn').filter(nogtm=name).values()
        return datagtm

    # ----------------------------------Perhitungan Saran --------------------------------------------#

    def getAllPrs(self):
        listprs = []
        listkap = {}
        newkap = {}
        prs = Datacater.objects.using('pgn').order_by('waktu').values('idprs','flow','pressureoutlet')
        for i in prs:
            for k,v in i.items():
                if k == 'idprs':
                    kap = Masterprs.objects.using('pgn').get(id=v).kapasitas
                    kapasitas = Masterprs.objects.using('pgn').get(id=v).kapasitas
                    temkap = 0
                    if kapasitas == 40:
                        temkap = 19
                    elif kapasitas == 20:
                        temkap = 9.5
                    elif kapasitas == 10:
                        temkap = 5
                    else:
                        temkap = 2.5
                    listkap['kap'] = temkap
                    newkap['kapasitas'] = kap
                newdict = {**i,**newkap,**listkap}
            listprs.append(newdict)
        return listprs

    def calculateSurv(self):
        tempsvt = {}
        listnewsvt = []
        temp = self.getAllPrs()
        tempkap = {}
        temppres = 0
        tempid = {}
        tempcap = 0
        tempflow = 0
        tempka = {}
        for i in temp:
            idprs = ""
            for k, v in i.items():
                if k == 'idprs':
                    idprs = v
                elif k == 'flow':
                    tempflow = float(v)
                elif k == 'pressureoutlet':
                    temppres = float(v)
                elif k == 'kap':
                    tempcap = int(v)
                elif k == 'kapasitas':
                    tempka['kapasitas'] = v
            svt = (temppres*tempcap)/tempflow
            tempid['id'] = idprs
            tempsvt['survival'] = svt
            newtems = {**tempid, **tempsvt, **tempka}
            listnewsvt.append(newtems)
        return listnewsvt


    def showcater_prs(self, prs, ms, nama):
        #all Prs datacater

        testemp = self.calculateSurv()
        jarak = 0
        tempj = {}
        newlist = []
        for i in testemp:
            for k,v in i.items():
                if k == 'id':
                    jarak = self.getJarakMs(ms=ms,prs=v)/20
                    tempj['jarak'] = jarak
                newdict = {**i, **tempj}
            newlist.append(newdict)
        print(newlist)



        gtmdict = {}
        idgtm = Mastergtm.objects.using('pgn').get(nogtm=nama).id
        kapgtm = Mastergtm.objects.using('pgn').get(id=idgtm).kapasitasgtm
        gtmdict['id'] = idgtm
        gtmdict['kap'] = kapgtm


        solusi = {}
        # print(gtmdict['kap'])
        for j in newlist:
            for k,v in j.items():
                if k == 'kapasitas':
                    if v == gtmdict['kap']:
                        print(v)


        #gtm standby di ms

        #kapasitas GTM

        print(idgtm)
        #jarak antara ms = prs
        jarak = self.getJarakMs(ms=ms,prs=prs)



        # querycater = Datacater.objects.using('pgn').filter(idprs=prs.id).values()

        # querycater = Datacater.query.
        # for i in querycater.values():
        #     return print(i)

        #TODO : Join
        # psobjs = Affiliation.objects.filter(ipId=x)
        # queryset = Sessions.objects.filter(sessionId__in=psobjs.values('sessionId'))





