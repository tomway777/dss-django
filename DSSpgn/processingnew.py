from DSSpgn.models_pgn import Datacater, Datagtm, Detaildatacater, Masterprs, Mastermotherstation, Mastergtm, Masterstatus
import operator

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
        mon, sec = divmod(time, 60)
        hr, mon = divmod(mon, 60)
        result = "%d:%02d:%02d" % (hr, mon, sec)
        return result


    def getDataPrs(self):
        dc = Datacater.objects.using('pgn').raw('(SELECT * FROM `datacater` where Waktu in '
                                                '(select MAX(Waktu) from datacater where Actived=1 group by IdPRS) and Actived=1 group by IdPRS)')
        listData = []

        for i in dc:
            dicttemp = {}
            prs = Masterprs.objects.using('pgn').get(id=i.idprs).namaprs
            flow = Detaildatacater.objects.using('pgn').get(idprs=i.idprs, iddc=i.id).flow
            gtm = Mastergtm.objects.using('pgn').get(id=i.idgtm).kapasitasgtm
            waktutempuh = Datagtm.objects.using('pgn').get(idgtm=i.idgtm).waktutempuh
            presgtm = i.pressuregtm
            newkap = self.convertKap(gtm)

            if(flow == 0):
                survival = ((presgtm*newkap)/1)*3600
            else:
                survival = ((presgtm*newkap)/flow)*3600
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
        waktutmp = Datagtm.objects.using('pgn').get(idgtm=idgtm).waktutempuh

        first_filter = []
        altsol = {}
        solusi = []
        for i in surv:
            if (waktutmp+1) <= i.get('survival')/3600 and i.get('kapasitas') == kap:
                first_filter.append(i)
                altsol[i.get('namaprs')] = i.get('waktutempuh')

        sorted_x = sorted(altsol.items(), key=operator.itemgetter(1))

        # count = len(first_filter)
        #
        # if count > 1:
        #     templis =[]
        #     for j in first_filter:
        #         templis.append(j.get('waktutempuh'))
        #     minx = min(templis)
        #     for k in surv:
        #         if k.get('waktutempuh') == minx:
        #             solusi.append(k)
        # else:
        #     solusi.append(first_filter)

        return sorted_x

    def getAltsolusi(self, namaprs):


        listsol = []
        surv = self.getDataPrs()
        for i in surv:
            for k in namaprs:
                if i.get('namaprs') == k[0]:
                    listsol.append(i)
        return listsol
