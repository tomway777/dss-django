from DSSpgn.models_pgn import Datacater,Masterprs, Mastergtm, Mastermotherstation, Datagtm, Masterstatus, Detaildatams
from DSSpgn.models import Datadetailprs, post_record
from decimal import Decimal
class process():
    def calculateSVT(self, flow, pressure, capacity):
        calc =  Decimal((pressure * capacity) / (flow/24)*60)
        return round(calc,2)
    #-------------------------------------------------------------Khusus-------#
    def getAllprs_nonsol(self):
        prs = Masterprs.objects.using('pgn').all().values()
        return prs
    # -------------------------------------------------------------Khusus-------#

    def convertKap(self, kapasitas):
        if kapasitas == 40:
            temkap = 19
        elif kapasitas == 20:
            temkap = 9.5
        elif kapasitas == 10:
            temkap = 5
        else:
            temkap = 2.5
        return temkap
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
        listkap = {}
        listbaru = []

        prs = Datacater.objects.using('pgn').all().order_by('waktu').values('idprs','idgtm','flow','pressureoutlet')
        #print(prs)



        listdict = list(prs)
        for i in listdict:
            for k,v in i.items():
                if k == 'idprs':
                    listnama['namaprs'] = self.getPrsName(v)
                if k == 'idgtm':
                    kapasitas = Mastergtm.objects.using('pgn').get(id=v).kapasitasgtm
                    kap = self.convertKap(kapasitas)
                    listkap['kapasitas'] = kapasitas
                    listkap['conkap'] =  kap
                    templist = {**i, **listnama, **listkap}
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
        namapr = {}
        newkap = {}
        prs = Datacater.objects.using('pgn').order_by('waktu').values('idprs','flow','pressureoutlet')
        for i in prs:
            for k,v in i.items():
                if k == 'idprs':
                    namaprs = Masterprs.objects.using('pgn').get(id=v).namaprs
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
                    namapr['namaprs'] = namaprs
                    listkap['kap'] = temkap
                    newkap['kapasitas'] = kap
                newdict = {**i,**namapr,**newkap,**listkap}
            listprs.append(newdict)
        # print(listprs)
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
        tempnama = {}
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
                elif k == 'namaprs':
                    tempnama['namaprs'] = v
            svt = (temppres*tempcap)/tempflow
            tempid['id'] = idprs
            tempsvt['survival'] = svt
            newtems = {**tempid, **tempnama, **tempsvt, **tempka}
            listnewsvt.append(newtems)
        return listnewsvt


    def showcater_prs(self,  ms, nama):
        #all Prs datacater

        testemp = self.calculateSurv()
        tempj = {}
        newlist = []
        for i in testemp:
            for k,v in i.items():
                if k == 'id':
                    jarak = self.getJarakMs(ms=ms,prs=v)/20
                    tempj['jarak'] = jarak
                newdict = {**i, **tempj}
            newlist.append(newdict)
        # print(newlist)

        gtmdict = {}
        idgtm = Mastergtm.objects.using('pgn').get(nogtm=nama).id
        kapgtm = Mastergtm.objects.using('pgn').get(id=idgtm).kapasitasgtm
        gtmdict['id'] = idgtm
        gtmdict['kap'] = kapgtm


        solusi = {}
        # print(gtmdict['kap'])
        # temr = []
        
        filter_first = []
        for x in newlist:
            if x.get('jarak') + 1 <= x.get('survival'):
                filter_first.append(x)
        print(filter_first)

        listsol = []
        for j in newlist:
            if j.get('kapasitas') == gtmdict['kap']:
                listsol.append(j)
        count = len(listsol)
        if count > 1:
            temsol = []
            listc = []
            for i in listsol:
                for k,v in i.items():
                    if k == 'jarak':
                        temsol.append(v)
            min_var = min(temsol)
            for j in listsol:
                if j.get('jarak') == min_var:
                    listc.append(j)
            solusi = listc
        else:
            solusi = listsol

        return solusi



        #TODO : Join
        # psobjs = Affiliation.objects.filter(ipId=x)
        # queryset = Sessions.objects.filter(sessionId__in=psobjs.values('sessionId'))





