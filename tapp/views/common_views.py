from django.shortcuts import render, redirect, HttpResponse
from tapp.models import district as dist, locations as loc, feedback as fd, login as log, user as usr

def index(request):
    datast = dist.objects.all()
    return render(request,"index.html",{"datast":datast})

def privacy(request):
    msg=""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session['id']
        data=log.objects.get(logid=id)
        if data.password==t1:
            msg="sucessfully updated"
            log.objects.filter(logid=id).update(password=t2)
        else:
            msg="invalid current password"

    returnpage="adminhome.html"

    if(request.session.get("role","")=="admin"):
        return redirect("/index")
    elif(request.session.get("role","")=="user"):
        returnpage="userhome.html"
    elif(request.session.get("role","")=="shop"):
        returnpage="shophome.html"
    elif(request.session.get("role","")=="club"):
        returnpage="shophome.html"
    elif(request.session.get("role","")=="turf"):
        returnpage="turfhome.html"
    return render(request,"privacy.html",{"role":returnpage,"msg":msg})

#district and location

def add_district(request):
    msg=""
    if request.POST:
        t1=request.POST["district"]
        dist.objects.create(district=t1)
        msg="inserted successfully"
    return render(request,"add_district.html",{"msg":msg})
    
def list_district(request):
    datalst=dist.objects.all()
    return render(request,"list_district.html",{"data":datalst})

def getLocation(request):
    id=request.GET["id"]
    datast=dist.objects.get(district_id=id)
    datadt=loc.objects.filter(district=datast).all()
    res="<option value=''>-select-</option>"
    for d in datadt:
        res+="<option value='"+str(d.location_id)+"'>"+d.location+"</option>"
    return HttpResponse(res)


def add_location(request):
    msg=""
    data=dist.objects.all()
    if request.POST:
        t1=request.POST["district"]
        t2=request.POST["location"]
        datadt=dist.objects.get(district_id=t1)
        loc.objects.create(district=datadt,location=t2)
        msg="inserted successfully"
    return render(request,"add_location.html",{"msg":msg,"data":data})

def list_location(request):
    data=loc.objects.all()
    dataldt=dist.objects.all()
    return render(request,"list_location.html",{"data":data,"datas":dataldt})

def edit_location(request):
    id=request.POST["location_id"]
    district=request.POST["location"]
    district_id=request.POST["district"]
    district=dist.objects.get(district_id=district_id)
    loc.objects.filter(location_id=id).update(location=district)
    response = redirect("/list_location")
    return response

def delete_location(request):
    id=request.POST["location_id"]
    loc.objects.filter(location_id=id).delete()
    response = redirect("/list_location")
    return response

def delete_dis(request):
    id=request.POST["s_id"]
    dist.objects.filter(district_id=id).delete()
    response = redirect("/list_district")
    return response
