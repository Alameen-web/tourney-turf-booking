from django.shortcuts import render, redirect
from tapp.models import turf as turf_model, login as log, district as dist, locations as loc, package as pack, pbooking as pbook, turfcomplaint as tcomp, rentitems as ritem, rentbookings as rbook
from datetime import date

# Note: Renaming models import to turf_model to avoid conflict with function name if any, primarily distinct usage

def turfreg(request):
    turf_name=request.POST["turf_name"]
    turf_address=request.POST["turf_address"]
    turf_phone=request.POST["turf_phone"]
    turf_email=request.POST["turf_email"]
    turf_district=request.POST["district"]
    did=dist.objects.get(district_id=turf_district)
    turf_location=request.POST["location"]
    sid=loc.objects.get(location_id=turf_location)
    username=request.POST["username"]
    password=request.POST["password"]
    log.objects.create(username=username,password=password,role="")
    datal=log.objects.last()
    turf_model.objects.create(login=datal,turf_name=turf_name,turf_address=turf_address,turf_phone=turf_phone,turf_email=turf_email,district=did,locations=sid,status="waiting")
    response = redirect('/index')
    return response

def turfhome(request):
    return render(request,"turfhome.html")

def turfPrivacy(request):
    msg = ""
    if request.POST:
        t1=request.POST["cpass"]
        t2=request.POST["npass"]

        id=request.session['id']
        data=log.objects.get(logid=id)
        if data.password==t1:
            msg="Password updated"
            log.objects.filter(logid=id).update(password=t2)
        else:
            msg="invalid current password"

    return render(request,"turfPrivacy.html",{"msg":msg})

def turfRegisterPackage(request):
    msg = ""
    return render(request,"turfRegisterPackage.html",{"msg":msg})

def turfRegisterPackageProcess(request):
    name=request.POST["name"]
    rate=request.POST["rate"]
    type=request.POST["type"]
    photo=request.FILES["photo"]
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    pack.objects.create(pack_name=name,pack_rate=rate,pack_type=type,pack_image=photo,pack_turf=logdata,pack_status="waiting")
    response = redirect('/turfRegisterPackage')
    return response

def turfPackageList(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = pack.objects.filter(pack_turf=logdata)
    return render(request,"turfPackageList.html",{"msg":msg,"data":data})

def turfPackageUpdate(request):
    if request.POST:
        packid = request.POST['packid']
        name = request.POST.get('pname',False)
        rate = request.POST.get('prate',False)
        type = request.POST.get('ptype',False)
        
        pack.objects.filter(packid=packid).update(pack_name=name,pack_rate=rate,pack_type=type)

    response = redirect('/turfPackageList')
    return response

def turfPackageDelete(request):
    if request.POST:
        packid = request.POST['packid']
        pack.objects.filter(packid=packid).delete()
    response = redirect('/turfPackageList')
    return response

def turfPackageNewBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="waiting")
    return render(request,"turfPackageNewBookings.html",{"msg":msg,"data":data})

def turfPackageBookingApprove(request):
    if request.POST:
        pbookid = request.POST['pbookid']
        pbook.objects.filter(pbookid=pbookid).update(status="approved")
    response = redirect('/turfPackageNewBookings')
    return response

def turfPackageBookingReject(request):
    if request.POST:
        pbookid = request.POST['pbookid']
        pbook.objects.filter(pbookid=pbookid).update(status="cancelled")
    response = redirect('/turfPackageNewBookings')
    return response

def turfPackageApprovedBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="approved")
    return render(request,"turfPackageApprovedBookings.html",{"msg":msg,"data":data})

def turfPackageRescheduleRequests(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="reschedule")
    return render(request,"turfPackageRescheduleRequests.html",{"msg":msg,"data":data})

def turfPackageRescheduleApprove(request):
    if request.POST:
        pbookid = request.POST['pbookid']
        pbook.objects.filter(pbookid=pbookid).update(status="confirm")
    response = redirect('/turfPackageRescheduleRequests')
    return response

def turfPackageRescheduleReject(request):
    if request.POST:
        pbookid = request.POST['pbookid']
        pbook.objects.filter(pbookid=pbookid).update(status="reject")
    response = redirect('/turfPackageRescheduleRequests')
    return response
    
def turfPackageRescheduledBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="confirm")
    return render(request,"turfPackageRescheduledBookings.html",{"msg":msg,"data":data})
    
def turfPackageCancelledBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="cancelled")
    return render(request,"turfPackageCancelledBookings.html",{"msg":msg,"data":data})
    
def turfComplaints(request):
    msg = ""
    logid = request.session['id']
    logdata = turf_model.objects.get(login=logid)
    data = tcomp.objects.filter(turf=logdata)
    return render(request,"turfComplaints.html",{"msg":msg,"data":data})
    
def turfAddComplaint(request):
    if request.POST:
        logid = request.session['id']
        logdata = turf_model.objects.get(login=logid)
        today = date.today()

        subject = request.POST['subject']
        complaint = request.POST['complaint']
        tcomp.objects.create(tsubject=subject,tmsg=complaint,tcomplaint_date=today,turf_id=logdata.turf_id)
    response = redirect('/turfComplaints')
    return response
    
def turfProfile(request):
    msg = ""
    logid = request.session['id']
    data = turf_model.objects.get(login=logid)
    return render(request,"turfProfile.html",{"msg":msg,"data":data})
    
def turfProfileUpdate(request):
    if request.POST:
        logid = request.session['id']
        turfid = request.POST['turfid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        owner = request.POST['owner']
        size = request.POST['size']

        turf_model.objects.filter(turf_id=turfid).update(turf_name=name,turf_email=email,turf_phone=phone,turf_address=address,turf_ownername=owner,turf_squarefeet=size)
    response = redirect('/turfProfile')
    return response



def turf_feed(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        tcomp.objects.filter(tcomplaint_id=t1).update(creply=t2)
    data=tcomp.objects.all()
    return render(request,"turf_feed.html",{"data":data})
