from DSSpgn.models_pgn import Datacater, Datagtm, Detaildatacater, Masterprs, Mastermotherstation, Mastergtm

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
            presgtm = i.pressuregtm
            newkap = self.convertKap(gtm)

            if(flow == 0):
                survival = self.convertime(((presgtm*newkap)/1)*3600)
            else:
                survival = self.convertime(((presgtm*newkap)/flow)*3600)


            dicttemp['namaprs'] = prs
            dicttemp['survival'] = survival
            dicttemp['kapasitas'] = gtm
            listData.append(dicttemp)
        # for i in prs:
        #     print(i)
        return listData

    def getGtmstandby(self, ms):
        gtmcurr = Datagtm.objects.using('pgn').filter(status=1,idms=ms).values()
        for i in gtmcurr:
            print(i.waktutempuh)