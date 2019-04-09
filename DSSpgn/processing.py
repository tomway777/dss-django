from DSSpgn.models_pgn import Datacater, Datams, Datagtm
from DSSpgn.models import Datadetailprs, post_record

class process():
    def calculateSVT(self):
        flow = Datacater.objects.using('pgn').latest('id').flow
        pressure = Datacater.objects.using('pgn').latest('id').pressureoutlet
        capacity = Datacater.objects.using('pgn').latest('id').pressuregtm
        calc =  (pressure * (capacity/200)) / flow
        return calc