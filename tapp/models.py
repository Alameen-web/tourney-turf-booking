from django.db import models
from datetime import date

class turfcomplaint(models.Model):
    tcomplaint_id = models.AutoField(primary_key=True)
    tsubject = models.CharField("tsubject",max_length=100)
    tmsg = models.CharField("tmsg",max_length=300)
    tcomplaint_date = models.CharField("tcomplaint_date",max_length=100)
    turf = models.ForeignKey("turf",on_delete=models.CASCADE, null=True)
    creply = models.CharField("creply",max_length=300,default="pending")

class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=100)
    password = models.CharField("password",max_length=100)
    role=models.CharField('role',max_length=10)

class turf(models.Model):
    turf_id=models.AutoField(primary_key=True)
    turf_name=models.CharField("turf_name",max_length=100)
    turf_phone=models.CharField("turf_phone",max_length=100)
    turf_email=models.CharField("turf_email",max_length=100)
    turf_address=models.CharField("turf_address",max_length=300)
    turf_squarefeet=models.CharField("turf_squarefeet",max_length=100)
    turf_ownername=models.CharField("turf_ownername",max_length=100)
    district=models.ForeignKey("district",on_delete=models.CASCADE, null=True)
    locations=models.ForeignKey("locations",on_delete=models.CASCADE, null=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    status=models.CharField("status",max_length=100)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField("user_name",max_length=100)
    user_phone=models.CharField("user_phone",max_length=100)
    user_email=models.CharField("user_email",max_length=100)
    user_contact=models.CharField("user_contact",max_length=100)
    district=models.ForeignKey("district",on_delete=models.CASCADE, null=True)
    locations=models.ForeignKey("locations",on_delete=models.CASCADE, null=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    status=models.CharField("status:",max_length=100)

class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    title = models.CharField("title",max_length=100)
    msg = models.CharField("msg",max_length=300)
    reply = models.CharField("reply",max_length=300,default="pending")

class package(models.Model):
    packid = models.AutoField(primary_key=True)
    pack_name = models.CharField("pack_name",max_length=100)
    pack_rate = models.IntegerField()
    pack_type = models.CharField("pack_type",max_length=100)
    pack_image = models.FileField("pack_image",max_length=500,upload_to="packages/")
    pack_turf = models.ForeignKey(turf,on_delete=models.CASCADE,null=True)
    pack_status = models.CharField("pack_status",max_length=100)

class pbooking(models.Model):
    pbookid = models.AutoField(primary_key=True)
    package = models.ForeignKey(package,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    date = models.CharField("date",max_length=100)
    turf = models.ForeignKey(turf,on_delete=models.CASCADE,null=True)
    status = models.CharField("status",max_length=100)
    
class district(models.Model):
    district_id = models.AutoField(primary_key=True)
    district = models.CharField("district",max_length=100)

class locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField("location",max_length=100)
    district = models.ForeignKey(district,on_delete=models.CASCADE,null=True)




    
# Create your models here.
