from DSSpgn.models_pgn import Datacater,Masterprs, Mastergtm, Mastermotherstation, Datagtm, Masterstatus
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
        if ms == 'SPBG':
            jarak = Datadetailprs.objects.get(nama=prs).spbg_ngagel
            return jarak/20.0
        elif ms == 'Indogas':
            jarak = Datadetailprs.objects.get(nama=prs).indogas_ikd_porong
            return jarak/20.0
        elif ms == 'Jes':
            jarak = Datadetailprs.objects.get(nama=prs).kso_dg_gagas
            return jarak/20.0
        else:
            jarak = Datadetailprs.objects.get(nama=prs).spbg_purwakarta
            return jarak/20.0

    # ----------------------------------Ambil GTM Standby--------------------------------------------#
    def getGTMStanby(self, ms=None):
        tempdict = {}
        comdict = {}
        listbaru = []
        currGTM = Datagtm.objects.using('pgn').filter(status=2, iddatams=ms) #ambil status gtm standby di ms
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
        # return listbaru
        # for i in currGTM.values():
        #     for k,v in i.items():
        #         if k == 'idprs':
        #             prsname = Masterprs.objects.using('pgn').get(id=v).namaprs
        # return currGTM

    # ----------------------------------Perhitungan Saran --------------------------------------------#

    def showcater_prs(self):
        prs = Masterprs.objects.using('pgn').get(id=2)
        querycater = Datacater.objects.using('pgn').filter(idprs=prs.id).values()

        # querycater = Datacater.query.
        # for i in querycater.values():
        #     return print(i)

        #TODO : Join
        # psobjs = Affiliation.objects.filter(ipId=x)
        # queryset = Sessions.objects.filter(sessionId__in=psobjs.values('sessionId'))





