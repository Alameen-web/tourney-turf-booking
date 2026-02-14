from django.shortcuts import render, redirect, HttpResponse
from tapp.models import user as usr, feedback as fd, login as log, district as dist, locations as loc, turf, package as pack, pbooking as pbook

def userreg(request):
    user_name=request.POST["user_name"]
    user_phone=request.POST["user_phone"]
    user_email=request.POST["user_email"]
    user_contact=request.POST["user_contact"]
    user_district=request.POST["district"]
    did=dist.objects.get(district_id=user_district)
    user_location=request.POST["location"]
    sid=loc.objects.get(location_id=user_location)
    username=request.POST["username"]
    password=request.POST["password"]
    log.objects.create(username=username,password=password,role="user")
    datal=log.objects.last()
    usr.objects.create(login=datal,user_name=user_name,user_phone=user_phone,user_email=user_email,user_contact=user_contact,district=did,locations=sid,status="waiting")
    response = redirect('/index')
    return response

def userhome(request):
    return render(request,"userhome.html")

def usershome(request):
    return render(request,"usershome.html")

def userFeedback(request):
    msg = ""
    logid = request.session['id']
    logdata = usr.objects.get(login=logid)
    data = fd.objects.filter(user_id=logdata)
    return render(request,"feedback.html",{"msg":msg,"data":data})
    
def userAddFeedback(request):
    if request.POST:
        logid = request.session['id']
        logdata = usr.objects.get(login=logid)
       

        t1=request.POST["title"]
        t2=request.POST["msg"]
        fd.objects.create(title=t1,msg=t2,user_id=logdata)
    response = redirect('/userFeedback')
    return response

def user_feedback(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        fd.objects.filter(feedback_id=t1).update(reply=t2)
    data=fd.objects.all()
    return render(request,"user_feed.html",{"data":data})

def userPrivacy(request):
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

    return render(request,"userPrivacy.html",{"msg":msg})

def searchturf(request): 
    datashp=turf.objects.filter(status="approved").all()
    return render(request,"allturfs.html",{"data":datashp})

def book(request):
    s1 = request.GET.get("s1")
    if not s1:
        return HttpResponse("Turf ID not provided", status=400)
    
    try:
        data = turf.objects.get(turf_id=s1)
        packages = pack.objects.filter(pack_turf=data)  # Fetch packages for the turf
        
        if request.method == 'POST':
            selected_turf = turf.objects.get(turf_id=s1)
            user_id = request.session['id']
            selected_user = usr.objects.get(login=user_id)
            pack_id = request.POST.get("pack_id")
            selected_package = pack.objects.get(packid=pack_id)
            booking_date = request.POST.get("booking_date")
            
            # Create a new booking record
            pbook.objects.create(
                package=selected_package,
                user=selected_user,
                date=booking_date,
                turf=selected_turf,
                status='waiting'  # Or any other status you wish to set
            )
            return redirect('searchturf')  # Redirect to the same page to avoid form resubmission
            
        return render(request, "bookturf.html", {"d": data, "s1": s1, "packages": packages})
    
    except turf.DoesNotExist:
        return HttpResponse("Turf not found", status=404)

def bookturf(request):
    s1=request.GET["s1"]
    
    datajob=turf.objects.get(turf_id=s1)
    dl=log.objects.get(logid=request.session["id"])
    dataapp=usr.objects.get(logid=dl)
    usr.objects.create(user_id=dataapp,turf_id=datajob)
    response = redirect('/book')
    return response

def usrPackageNewBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = usr.objects.get(login=logid)
    data = pbook.objects.filter(user=logdata,status="waiting")
    return render(request,"usrPackageNewBookings.html",{"msg":msg,"data":data})

def usrPackageApprovedBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = usr.objects.get(login=logid)
    data = pbook.objects.filter(user=logdata,status="approved")
    return render(request,"usrPackageNewBookings.html",{"msg":msg,"data":data})

def usrPackageCancelledBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = usr.objects.get(login=logid)
    data = pbook.objects.filter(user=logdata,status="cancelled")
    return render(request,"usrPackageNewBookings.html",{"msg":msg,"data":data})




