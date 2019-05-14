from DSSpgn.models_pgn import Datacater,Masterprs, Mastergtm, Mastermotherstation, Datagtm, Masterstatus, Detaildatams
from DSSpgn.processing import process

class olah():
    def getData(self, msid=None):
        gtm = Mastergtm.objects.using('pgn').filter(status=1).values()
        ms = Mastermotherstation.objects.using('pgn').get(id=msid)
        pro = process()
        prs = pro.calculateSurv()
        tempj = {}
        newlist = []
        for i in prs:
            for k, v in i.items():
                if k == 'id':
                    jarak = pro.getJarakMs(ms=msid, prs=v) / 20
                    tempj['jarak'] = jarak
                newdict = {**i, **tempj}
            newlist.append(newdict)


