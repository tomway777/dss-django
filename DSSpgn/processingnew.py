from DSSpgn.models_pgn import Datacater, Datagtm, Detaildatacater, Masterprs, Mastermotherstation, Mastergtm, Masterstatus
import operator
from math import floor
from datetime import datetime, date


class processingnew():

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

    def convertime(self,time):
        detik = time
        d = floor(detik / (60 * 60 * 24))
        detik -= d * (60 * 60 * 24)
        h = floor(detik / 3600)
        detik -= h * (3600)
        m = floor(detik / 60)
        detik -= m * 60
        s = floor(detik)
        detik -= s
        result = "%dd %02d:%02d:%02d" % (d, h, m, s)
        return result


    def getDataPrs(self):
        dc = Datacater.objects.using('pgn').raw('(SELECT * FROM `datacater` where Waktu in '
                                                '(select MAX(Waktu) from datacater where Actived=1 group by IdPRS) and Actived=1 group by IdPRS)')
        tempwaktu = {}
        for k in dc:
            waktu = Datacater.objects.using('pgn').filter(idprs=k.idprs).order_by('-waktu')
            if waktu.__len__() > 1:
                tempwaktu[k.idprs] = ((waktu[0].waktu - waktu[1].waktu).seconds)/3600
                # print(((waktu[0].waktu - waktu[1].waktu).seconds)/3600)
            else:
                tempwaktu[k.idprs] = 1
        # print(tempwaktu)

        listData = []

        for i in dc:
            dicttemp = {}
            prs = Masterprs.objects.using('pgn').get(id=i.idprs).namaprs
            flow = Detaildatacater.objects.using('pgn').get(idprs=i.idprs, iddc=i.id).flow
            gtm = Mastergtm.objects.using('pgn').get(id=i.idgtm).kapasitasgtm
            # waktutempuh = Datagtm.objects.using('pgn').get(idgtm=i.idgtm).get_latest_by('-waktu').waktutempuh
            waktutempuh = Datagtm.objects.using('pgn').filter(idgtm=i.idgtm).latest('-tanggal').waktutempuh
            wflow = tempwaktu.get(i.idprs)
            presgtm = i.pressuregtm
            newkap = self.convertKap(gtm)

            if(flow == 0):
                survival = ((presgtm*newkap)/1)*3600
            else:
                survival = ((presgtm*newkap)/(flow/wflow))*3600
            dicttemp['convsur'] = self.convertime(survival)
            dicttemp['idgtm'] = i.idgtm
            dicttemp['namaprs'] = prs
            dicttemp['survival'] = survival
            dicttemp['kapasitas'] = gtm
            dicttemp['waktutempuh'] = waktutempuh
            listData.append(dicttemp)
        # for i in prs:
        #     print(i)
        return listData

    def getGtmstandby(self):
        gtmcurr = Datagtm.objects.using('pgn').all()
        listgtm = []

        for i in gtmcurr:
            tempdict = {}
            nogtm = Mastergtm.objects.using('pgn').get(id=i.idgtm).nogtm
            kapasitas = Mastergtm.objects.using('pgn').get(id=i.idgtm).kapasitasgtm
            status = Masterstatus.objects.using('pgn').get(id=i.status).namastatus
            if(i.status > 3 and i.status < 9):
                prs = Masterprs.objects.using('pgn').get(id=i.idprs).namaprs
                tempdict['lokasi'] = prs
            else:
                ms = Mastermotherstation.objects.using('pgn').get(id=i.idms).namams
                tempdict['lokasi'] = ms

            tempdict['nogtm'] = nogtm
            tempdict['kapasitas'] = kapasitas
            tempdict['status'] = status
            listgtm.append(tempdict)


        return listgtm

    def getGTMstanby(self, ms=None):
        gtm = Datagtm.objects.using('pgn').raw('SELECT datagtm.Id, IdMS, IdGTM, NamaStatus, NoGTM, KapasitasGTM FROM datagtm '
                                               'LEFT JOIN masterstatus ON datagtm.Status = masterstatus.Id LEFT JOIN '
                                               'mastergtm ON datagtm.IdGTM = mastergtm.Id WHERE IdMS = %s', [ms])

        return gtm



    def showSaran(self, ms, id):
        idgtm = Mastergtm.objects.using('pgn').get(nogtm=id, actived=1).id
        kap = Mastergtm.objects.using('pgn').get(id=idgtm).kapasitasgtm
        surv = self.getDataPrs()
        # waktutmp = Datagtm.objects.using('pgn').get(idgtm=idgtm).waktutempuh
        waktutmp = Datagtm.objects.using('pgn').filter(idgtm=idgtm).latest('-tanggal').waktutempuh
        first_filter = []
        altsol = {}
        solusi = []
        for i in surv:
            if (waktutmp+1) <= i.get('survival')/3600 and i.get('kapasitas') == kap:
                first_filter.append(i)
                altsol[i.get('namaprs')] = i.get('waktutempuh')

        sorted_x = sorted(altsol.items(), key=operator.itemgetter(1))
        return sorted_x

    def getAltsolusi(self, namaprs):


        listsol = []
        surv = self.getDataPrs()
        for i in surv:
            for k in namaprs:
                if i.get('namaprs') == k[0]:
                    listsol.append(i)
        return listsol
