from django.http import HttpResponse,JsonResponse
from tapp.models import login as log, user as usr, district as dist, locations as loc, turf, package as pack, pbooking as pbook, rentitems as ritem, rentbookings as rbook 

from django.db.models import Q
from datetime import date
import json

def app_login(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    msg="try again later"
    c=log.objects.filter(username=t1,password=t2).count()
    if c == 1 : 
        dat=log.objects.get(username=t1,password=t2)
        if(dat.role == "user"):
            du=usr.objects.get(login=dat)
            if du.status == "waiting":
                msg="not yet verified"
            else :
                msg="ok:"+str(dat.logid)+":user:"+du.user_name+":"+str(du.district.district_id)+":"+str(du.locations.location_id)
        else:
            msg="invalid account Details"
    else:
         msg="invalid user name or password"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_register(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    t6=request.POST["t6"]
    t7=request.POST["t7"]

    dst = dist.objects.get(district_id=t4)
    loca = loc.objects.get(location_id=t5)

    log.objects.create(username=t6,password=t7,role="user")
    data=log.objects.last()
    usr.objects.create(user_name=t1,user_phone=t2,user_email=t3,district=dst,locations=loca, status="waiting",login=data)
    msg="ok:"+str(data.logid)
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_getdistrict(request):

    datar=dist.objects.values("district_id","district")
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def app_getlocation(request):
    t1 = request.POST["t1"]
    datax=dist.objects.get(district_id=t1)
    datar=loc.objects.filter(district=datax).values("location_id","location")
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def app_getUserProfile(request):
    user = usr.objects.filter(login = request.POST['t1']).values("user_id","user_name","user_phone","user_email")
    data=json.dumps(list(user))
    
    return HttpResponse(data, content_type="application/json")

def app_changePassword(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    data=log.objects.get(logid = t3)
    if data.password == t1:
        msg="ok"
        log.objects.filter(logid = t3).update(password = t2)
    else:
        msg="invalid current password"
    
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_getTurfList(request):
    t1 = request.POST["t1"]
    datax=dist.objects.get(district_id=t1)
    datar = turf.objects.filter(district=t1).all()
    
    db = []
    for d in datar:
        
        v = {
            "turf_id":str(d.turf_id),
            "turf_name":d.turf_name,
            "turf_phone":d.turf_phone,
            "turf_email":d.turf_email,
            "turf_address":d.turf_address,
            "turf_squarefeet":d.turf_squarefeet,
            "turf_ownername":d.turf_ownername,
            "district_id":str(d.district),
            "district":str(d.district.district),
            "locations_id":str(d.locations),
            "location":str(d.locations.location)
        }
        db.append(v)

    data=json.dumps(list(db))
    return HttpResponse(data, content_type="application/json")

def app_getTurfPackages(request):
    t1 = request.POST["t1"]
    datar = pack.objects.filter(pack_turf = t1, pack_status = "approved").values("packid","pack_name","pack_rate","pack_type","pack_status","pack_image","pack_turf_id")
    data=json.dumps(list(datar))
    
    return HttpResponse(data, content_type="application/json")

def app_bookPackage(request):
    t1 = request.POST["t1"] #date
    t2 = pack.objects.get(packid = request.POST["t2"])
    t3 = turf.objects.get(turf_id = request.POST["t3"])
    t4 = usr.objects.get(login = request.POST["t4"])

    pbook.objects.create(date = t1, status = "waiting", package = t2, turf = t3 ,user = t4)
    msg="ok"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_getPackageBookings(request):
    t1 = usr.objects.get(login = request.POST["t1"]) #date

    datar = pbook.objects.filter(user = t1).all()
    
    db = []
    for d in datar:
        
        v = {
            "pbookid":str(d.pbookid),
            "date":d.date,
            "status":d.status,
            "package_id":str(d.package),
            "turf_id":str(d.turf),
            "turf_name":str(d.turf.turf_name),
            "user_id":str(d.user),
            "pack_name":str(d.package.pack_name),
            "pack_type":str(d.package.pack_type),
            "pack_rate":str(d.package.pack_rate),
            "pack_status":str(d.package.pack_status),
            "pack_image":str(d.package.pack_image)
        }
        db.append(v)

    data=json.dumps(list(db))
    return HttpResponse(data, content_type="application/json")

def app_rescheduleBooking(request):
    t1 = request.POST["t1"] #pbookid
    t2 = request.POST["t2"] #date
    pbook.objects.filter(pbookid = t1).update(date = t2, status = "reschedule")
    msg="ok"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_cancelTurfBooking(request):
    t1 = request.POST["t1"] #pbookid
    pbook.objects.filter(pbookid = t1).update(status = "cancelled")
    msg="ok"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)
    
def app_getRentItems(request):
    t1 = request.POST["t1"] #turfid
    datar = ritem.objects.filter(rent_turf = t1, item_status = "approved").values("rentid","item_name","item_image","item_rph","item_status","rent_turf_id")
    data=json.dumps(list(datar))
    
    return HttpResponse(data, content_type="application/json")
    
def app_bookRentItem(request):
    t1 = ritem.objects.get(rentid = request.POST["t1"]) #rentitem
    t2 = usr.objects.get(login = request.POST["t2"]) #logid
    t3 = request.POST["t3"] #bdate
    t4 = request.POST["t4"] #btime
    t5 = turf.objects.get(turf_id = request.POST["t5"]) #turf
    rbook.objects.create(rent_item = t1, turf = t5, rent_hours = t4, rbook_date = t3 ,rent_user = t2, book_status = "waiting", pay_status = "waiting")
    
    msg="ok"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)
    
def app_getRentItemBookings(request):
    t1 = usr.objects.get(login = request.POST["t1"]) #date

    datar = rbook.objects.filter(rent_user = t1).all()
    
    db = []
    for d in datar:
        
        v = {
            "rbookid":str(d.rbookid),
            "rent_hours":d.rent_hours,
            "rbook_date":d.rbook_date,
            "book_status":str(d.book_status),
            "pay_status":str(d.pay_status),
            "rent_item_id":str(d.rent_item),
            "item_name":str(d.rent_item.item_name),
            "item_image":str(d.rent_item.item_image),
            "item_rph":str(d.rent_item.item_rph),
            "rent_user_id":str(d.rent_user),
            "turf_id":str(d.turf),
            "turf_name":str(d.turf.turf_name)
        }
        db.append(v)

    data=json.dumps(list(db))
    return HttpResponse(data, content_type="application/json")
    
def app_cancelItemBooking(request):
    t1 = request.POST["t1"] #rbookid
    rbook.objects.filter(rbookid = t1).update(book_status = "cancelled")
    msg="ok"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)
    
