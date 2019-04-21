# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class post_record(models.Model):
    id_post = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255)
    gtm = models.TextField(max_length=100)
    prs_tujuan = models.TextField(max_length=100)
    standby_time = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_post


class Datadetailprs(models.Model):
    id_prs = models.AutoField(primary_key=True)
    nama = models.TextField(blank=True, null=True)
    kategori_pelanggan = models.IntegerField(blank=True, null=True)
    harga = models.IntegerField(blank=True, null=True)
    produksi = models.IntegerField(blank=True, null=True)
    spbg_ngagel = models.IntegerField(db_column='SPBG_ngagel', blank=True, null=True)  # Field name made lowercase.
    indogas_ikd_porong = models.IntegerField(db_column='Indogas_IKD_porong', blank=True, null=True)  # Field name made lowercase.
    kso_dg_gagas = models.IntegerField(db_column='KSO_DG_Gagas', blank=True, null=True)  # Field name made lowercase.
    spbg_purwakarta = models.IntegerField(db_column='SPBG_purwakarta', blank=True, null=True)  # Field name made lowercase.
    sizegtm = models.TextField(db_column='SizeGTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datadetailprs'

