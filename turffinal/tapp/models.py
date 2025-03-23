from django.db import models

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
    
# class shop(models.Model):
#     shop_id=models.AutoField(primary_key=True)
#     shop_name=models.CharField("shop_name",max_length=100)
#     shop_phone=models.CharField("shop_phone",max_length=100)
#     shop_email=models.CharField("shop_email",max_length=100)
#     shop_address=models.CharField("shop_address",max_length=300)
#     district=models.ForeignKey("district",on_delete=models.CASCADE, null=True)
#     locations=models.ForeignKey("locations",on_delete=models.CASCADE, null=True)
#     login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
#     status=models.CharField("status",max_length=100)

# class club(models.Model):
#     club_id=models.AutoField(primary_key=True)
#     club_name=models.CharField("club_name",max_length=100)
#     club_phone=models.CharField("club_phone",max_length=100)
#     club_email=models.CharField("club_email",max_length=100)
#     club_address=models.CharField("club_address",max_length=300) 
#     club_banner=models.FileField("club_banner",max_length=100,upload_to="images/")
#     district=models.ForeignKey("district",on_delete=models.CASCADE, null=True)
#     locations=models.ForeignKey("locations",on_delete=models.CASCADE, null=True)
#     login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
#     status=models.CharField("status",max_length=100)

class district(models.Model):
    district_id=models.AutoField(primary_key=True)
    district=models.CharField("district",max_length=100)
    
class locations(models.Model):
    location_id=models.AutoField(primary_key=True)
    location=models.CharField("location",max_length=100)
    district=models.ForeignKey("district", on_delete=models.CASCADE, null=True)
    
# class feedback(models.Model):
#     feedback_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
#     title = models.CharField("title",max_length=200)
#     msg = models.CharField("message",max_length=500)
#     reply = models.CharField("reply",max_length=500)
    
# class turf(models.Model):
#     turf_id=models.AutoField(primary_key=True)
#     turf_name=models.CharField("turf_name",max_length=100)
#     turf_phone=models.CharField("turf_phone",max_length=100)
#     turf_email=models.CharField("turf_email",max_length=100)
#     turf_address=models.CharField("turf_address",max_length=300)
#     turf_squarefeet=models.CharField("turf_squarefeet",max_length=100)
#     turf_ownername=models.CharField("turf_ownername",max_length=100)
#     district=models.ForeignKey("district",on_delete=models.CASCADE, null=True)
#     locations=models.ForeignKey("locations",on_delete=models.CASCADE, null=True)
#     login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
#     status=models.CharField("status",max_length=100)

class package(models.Model):
    packid = models.AutoField(primary_key=True)
    pack_name = models.CharField("pack_name",max_length=100)
    pack_rate = models.IntegerField()
    pack_type = models.CharField("pack_type",max_length=100)
    pack_status = models.CharField("pack_status",max_length=100)
    pack_turf = models.ForeignKey("turf",on_delete=models.CASCADE, null=True)
    pack_image = models.FileField("pack_image",max_length=500,upload_to="package/")

class pbooking(models.Model):
    pbookid = models.AutoField(primary_key=True)
    package = models.ForeignKey("package",on_delete=models.CASCADE, null=True)
    user = models.ForeignKey("user",on_delete=models.CASCADE, null=True)
    date = models.CharField("date",max_length=100)
    turf = models.ForeignKey("turf",on_delete=models.CASCADE, null=True)
    status = models.CharField("status",max_length=100)

# class turfcomplaint(models.Model):
#     tcomplaint_id = models.AutoField(primary_key=True)
#     turf = models.ForeignKey(turf,on_delete=models.CASCADE,null=True)
#     tsubject = models.CharField("tsubject",max_length=200)
#     tmsg = models.CharField("tmessage",max_length=500)
#     creply = models.CharField("treply",max_length=500)
#     tcomplaint_date=models.CharField("tdate",max_length=100)

# class clubcomplaint(models.Model):
#     ccomplaint_id=models.AutoField(primary_key=True)
#     club_id = models.ForeignKey(club,on_delete=models.CASCADE,null=True)
#     csubject = models.CharField("csubject",max_length=200)
#     cmsg = models.CharField("cmessage",max_length=500)
#     creply = models.CharField("creply",max_length=500)
#     ccomplaint_date=models.CharField("cdate",max_length=100)

# class shopcomplaint(models.Model):
#     scomplaint_id=models.AutoField(primary_key=True)
#     shop_id = models.ForeignKey(shop,on_delete=models.CASCADE,null=True)
#     ssubject = models.CharField("ssubject",max_length=200)
#     smsg = models.CharField("smessage",max_length=500)
#     sreply = models.CharField("sreply",max_length=500)
#     scomplaint_date=models.CharField("sdate",max_length=100)

# class rentitems(models.Model):
#     rentid = models.AutoField(primary_key=True)
#     rent_turf = models.ForeignKey(turf,on_delete=models.CASCADE,null=True)
#     item_name = models.CharField("item_name",max_length=100)
#     item_image = models.FileField("item_image",max_length=500,upload_to="rentItems/")
#     item_rph = models.IntegerField()
#     item_status = models.CharField("item_status",max_length=100)

# class rentbookings(models.Model):
#     rbookid = models.AutoField(primary_key=True)
#     rent_item = models.ForeignKey(rentitems,on_delete=models.CASCADE,null=True)
#     turf = models.ForeignKey(turf,on_delete=models.CASCADE,null=True)
#     rent_hours = models.IntegerField()
#     rbook_date = models.CharField("rbook_date",max_length=100)
#     rent_user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
#     book_status = models.CharField("book_status",max_length=100)
#     pay_status = models.CharField("pay_status",max_length=100)

# class payments(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     rent_book = models.ForeignKey(rentbookings,on_delete=models.CASCADE,null=True)
#     amount = models.IntegerField()
#     pay_date = models.CharField("pay_status",max_length=100)

# class saleitem(models.Model):
#     sitem_id=models.AutoField(primary_key=True)
#     sitem_name=models.CharField("sitem_name",max_length=100)
#     sitem_photo=models.FileField("sitem_image",max_length=100,upload_to="item/")
#     sitem_description=models.CharField("sitem_description",max_length=500)
#     sitem_stock=models.IntegerField()
#     sitem_price=models.IntegerField()
#     shop = models.ForeignKey(shop,on_delete=models.CASCADE,null=True)
#     sitem_status = models.CharField("sitem_status",max_length=100)

# class stock(models.Model):
#     stock_id=models.AutoField(primary_key=True)
#     saleitem=models.ForeignKey("saleitem",on_delete=models.CASCADE, null=True)
#     stock_quantity=models.CharField("quantity",max_length=100)
#     stock_itemprice=models.CharField("price",max_length=100)
#     stock_itembrand=models.CharField("brand",max_length=100)
#     stock_status=models.CharField("stock_status",max_length=100)

# class tournament(models.Model):
#     tour_id=models.AutoField(primary_key=True)
#     tour_name=models.CharField("tour_name",max_length=100)
#     district=models.ForeignKey("district",on_delete=models.CASCADE, null=True)
#     locations=models.ForeignKey("locations",on_delete=models.CASCADE, null=True)
#     club=models.ForeignKey(club,on_delete=models.CASCADE,null=True)
#     tour_details=models.CharField("tour_details",max_length=500)
#     tour_venue=models.CharField("tour_venue",max_length=100)
#     tour_time=models.CharField("tour_time",max_length=100)
#     tour_date=models.CharField("tour_date",max_length=100)
#     ticketcharge=models.CharField("ticketcharge",max_length=100)
#     no_tickets=models.CharField("no_tickets",max_length=100)
#     tour_status=models.CharField("status",max_length=100)
#     soldcount=models.CharField("tickets sold",max_length=100)
    
# class ticketbooking(models.Model):
#     booking_id=models.AutoField(primary_key=True)
#     tour=models.ForeignKey(tournament,on_delete=models.CASCADE,null=True)
#     user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
#     bookdate=models.CharField("bookdate",max_length=100)
#     ticketcount=models.CharField("ticketcount",max_length=100)
#     ticket_status=models.CharField("ticket_status",max_length=100)
#     paydate=models.ForeignKey(payments,on_delete=models.CASCADE,null=True, related_name='payments1')
#     payamount=models.ForeignKey(payments,on_delete=models.CASCADE,null=True, related_name='payments2')

# class orders(models.Model):
#     order_id=models.AutoField(primary_key=True)
#     user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
#     shop=models.ForeignKey(shop,on_delete=models.CASCADE,null=True)
#     order_status=models.CharField("order_status",max_length=100)
#     @property
#     def getOrderItems(self):
#         return orderitem.objects.filter(order = self).all()

# class orderitem(models.Model):
#     order_itemid=models.AutoField(primary_key=True)
#     order=models.ForeignKey(orders,on_delete=models.CASCADE,null=True)
#     item=models.ForeignKey(saleitem,on_delete=models.CASCADE,null=True)
#     quantity=models.CharField("quantity",max_length=100)

    
# Create your models here.
