# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Datacater(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    idprs = models.IntegerField(db_column='IdPRS', blank=True, null=True)  # Field name made lowercase.
    idgtm = models.IntegerField(db_column='IdGTM', blank=True, null=True)  # Field name made lowercase.
    idht = models.IntegerField(db_column='IdHT', blank=True, null=True)  # Field name made lowercase.
    waktu = models.DateTimeField(db_column='Waktu', blank=True, null=True)  # Field name made lowercase.
    vbase = models.FloatField(db_column='VBase', blank=True, null=True)  # Field name made lowercase.
    vturbin = models.FloatField(db_column='Vturbin', blank=True, null=True)  # Field name made lowercase.
    flow = models.FloatField(db_column='Flow', blank=True, null=True)  # Field name made lowercase.
    temp = models.FloatField(db_column='Temp', blank=True, null=True)  # Field name made lowercase.
    pressureoutlet = models.FloatField(db_column='PressureOutlet', blank=True, null=True)  # Field name made lowercase.
    pressuregtm = models.FloatField(db_column='PressureGTM', blank=True, null=True)  # Field name made lowercase.
    tempgtm = models.FloatField(db_column='TempGTM', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datacater'


class Datagtm(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    iddatams = models.IntegerField(db_column='IdDataMs', blank=True, null=True)  # Field name made lowercase.
    idgtm = models.IntegerField(db_column='IdGTM', blank=True, null=True)  # Field name made lowercase.
    idht = models.IntegerField(db_column='IdHT', blank=True, null=True)  # Field name made lowercase.
    iddriver = models.IntegerField(db_column='IdDriver', blank=True, null=True)  # Field name made lowercase.
    tanggal = models.DateTimeField(db_column='Tanggal', blank=True, null=True)  # Field name made lowercase.
    idms = models.IntegerField(db_column='IdMS', blank=True, null=True)  # Field name made lowercase.
    idprs = models.IntegerField(db_column='IdPRS', blank=True, null=True)  # Field name made lowercase.
    jarak = models.FloatField(db_column='Jarak', blank=True, null=True)  # Field name made lowercase.
    jaraktempuh = models.FloatField(db_column='JarakTempuh', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datagtm'


class Datams(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    idms = models.IntegerField(db_column='IdMS', blank=True, null=True)  # Field name made lowercase.
    idgtm = models.IntegerField(db_column='IdGTM', blank=True, null=True)  # Field name made lowercase.
    idht = models.IntegerField(db_column='IdHT', blank=True, null=True)  # Field name made lowercase.
    iddriver = models.IntegerField(db_column='IdDriver', blank=True, null=True)  # Field name made lowercase.
    tanggalmasuk = models.DateField(db_column='Tanggalmasuk', blank=True, null=True)  # Field name made lowercase.
    do = models.CharField(db_column='DO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ghv = models.FloatField(db_column='GHV', blank=True, null=True)  # Field name made lowercase.
    pressureawal = models.FloatField(db_column='PressureAwal', blank=True, null=True)  # Field name made lowercase.
    pressureakhir = models.FloatField(db_column='PressureAkhir', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datams'


class Datatarget(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    jenistarget = models.CharField(db_column='JenisTarget', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nilai = models.FloatField(db_column='Nilai', blank=True, null=True)  # Field name made lowercase.
    tanggaltarget = models.CharField(db_column='TanggalTarget', max_length=10, blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datatarget'


class Detaildatams(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    iddatams = models.IntegerField(db_column='IdDataMs', blank=True, null=True)  # Field name made lowercase.
    idprs = models.IntegerField(db_column='IdPRS', blank=True, null=True)  # Field name made lowercase.
    jarak = models.FloatField(db_column='Jarak', blank=True, null=True)  # Field name made lowercase.
    jaraktempuh = models.FloatField(db_column='JarakTempuh', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detaildatams'


class Employee(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    married = models.CharField(db_column='Married', max_length=7, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Entrydatameter(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    idpelanggan = models.IntegerField(db_column='IdPelanggan', blank=True, null=True)  # Field name made lowercase.
    tanggal = models.DateField(db_column='Tanggal', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    nominasi = models.FloatField(db_column='Nominasi', blank=True, null=True)  # Field name made lowercase.
    target = models.FloatField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrydatameter'


class History(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idmodule = models.IntegerField(db_column='IdModule')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=6)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry')  # Field name made lowercase.
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'history'


class Masterdriver(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    namadriver = models.CharField(db_column='NamaDriver', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noktp = models.CharField(db_column='NoKTP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nohp = models.CharField(db_column='NoHP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterdriver'


class Mastergtm(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    nogtm = models.CharField(db_column='NoGTM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lwc = models.FloatField(db_column='LWC', blank=True, null=True)  # Field name made lowercase.
    kapasitasgtm = models.FloatField(db_column='KapasitasGTM', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mastergtm'


class Masterheadtruck(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    noht = models.CharField(db_column='NoHT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platno = models.CharField(db_column='PlatNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterheadtruck'


class Masterlokasipelanggan(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    idprs = models.IntegerField(db_column='IdPRS', blank=True, null=True)  # Field name made lowercase.
    idms = models.IntegerField(db_column='IdMS', blank=True, null=True)  # Field name made lowercase.
    jarak = models.FloatField(db_column='Jarak', blank=True, null=True)  # Field name made lowercase.
    waktunormal = models.FloatField(db_column='WaktuNormal', blank=True, null=True)  # Field name made lowercase.
    waktusedang = models.FloatField(db_column='WaktuSedang', blank=True, null=True)  # Field name made lowercase.
    waktupadat = models.FloatField(db_column='WaktuPadat', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterlokasipelanggan'


class Mastermotherstation(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    namams = models.CharField(db_column='NamaMS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kapasitasms = models.FloatField(db_column='KapasitasMS', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mastermotherstation'


class Masterpelanggan(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    idpelanggan = models.CharField(db_column='IdPelanggan', max_length=25, blank=True, null=True)  # Field name made lowercase.
    namapelanggan = models.CharField(db_column='NamaPelanggan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nilaikontrak = models.FloatField(db_column='NilaiKontrak', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt', blank=True, null=True)  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterpelanggan'


class Masterprs(models.Model):
    id = models.AutoField(db_column='Id',primary_key=True)  # Field name made lowercase.
    namaprs = models.CharField(db_column='NamaPRS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kapasitas = models.IntegerField(db_column='Kapasitas', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterprs'


class Masterstatus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    namastatus = models.CharField(db_column='NamaStatus', max_length=250, blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    udateat = models.DateTimeField(db_column='UdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived')  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'masterstatus'


class Module(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    parent = models.IntegerField(db_column='Parent')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'module'


class TypeUser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt')  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived')  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type_user'


class UserAccess(models.Model):
    idtypeuser = models.IntegerField(db_column='IdTypeUser', primary_key=True)  # Field name made lowercase.
    idmodule = models.IntegerField(db_column='IdModule')  # Field name made lowercase.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_access'
        unique_together = (('idtypeuser', 'idmodule'),)


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idemploye = models.IntegerField(db_column='IdEmploye')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    remember_token = models.CharField(db_column='Remember_Token', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typeuser = models.IntegerField(db_column='TypeUser')  # Field name made lowercase.
    apitoken = models.TextField(db_column='ApiToken', blank=True, null=True)  # Field name made lowercase.
    actived = models.IntegerField(db_column='Actived')  # Field name made lowercase.
    createat = models.DateTimeField(db_column='CreateAt')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='UpdateAt', blank=True, null=True)  # Field name made lowercase.
    userentry = models.IntegerField(db_column='UserEntry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
