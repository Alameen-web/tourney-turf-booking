from re import S
from this import s
from django.shortcuts import render, redirect, HttpResponse
import time
from datetime import date
import os
from .models import login as log, district as dist, locations as loc, user as usr 
from .models import turf , package as pack, pbooking as pbook



def index(request):
    datast = dist.objects.all()
    return render(request,"index.html",{"datast":datast})

# def adlogin(request):
#     return render(request,"adminlog.html")

def userlog(request):
    return render(request,"userlog.html")
 
def usershome(request):
    return render(request,"usershome.html")

def admin(request):
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        
        datac = log.objects.filter(username=user, password=password,role="admin").count()
        if datac==1:
                data=log.objects.get(username=user, password=password,role="admin")
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.logid
                response = redirect('/adminhome')
                return response
        else:
                 return render(request,"adminlog.html",{"msg":"invalid username or password"})
    else:
        return render(request,"adminlog.html",{"msg":""})
    
def adminhome(request):
    return render(request,"adminhome.html")

def stafflogin(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            datac = log.objects.filter(username=username, password=password).count()
            if datac==1:
                data=log.objects.get(username=username, password=password)
                if data.role=="turf":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/turfhome')
                    return response
                elif data.role=="user":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/userhome')
                    return response
                elif data.role=="shop":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/shophome')
                    return response
                elif data.role=="club":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/clubhome')
                    return response
                else :
                    response = redirect('/index?msg=invalid access')
                    return response


            else:
                response = redirect('/index?msg=invalid username or password')
                return response
               
        except:
            response = redirect('/index?msg=something went wrong')
            return response
    else:
        response = redirect('/index')
        return response
    
def userhome(request):
    return render(request,"userhome.html")

# def shophome(request):
#     return render(request,"shophome.html")

# def clubhome(request):
#     return render(request,"clubhome.html")

def turfhome(request):
    return render(request,"turfhome.html")

def logout(request):       
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index")
        return response
    except:
        response = redirect("/index")
        return response

# def privacy(request):
#     msg=""
#     if request.POST:
#         t1=request.POST["t1"]
#         t2=request.POST["t2"]
#         id=request.session['id']
#         data=log.objects.get(logid=id)
#         if data.password==t1:
#             msg="sucessfully updated"
#             log.objects.filter(logid=id).update(password=t2)
#         else:
#             msg="invalid current password"


   
#     returnpage="adminhome.html"

#     if(request.session.get("role","")=="admin"):
#         return redirect("/index")
#     elif(request.session.get("role","")=="user"):
#         returnpage="userhome.html"
#     elif(request.session.get("role","")=="shop"):
#         returnpage="shophome.html"
#     elif(request.session.get("role","")=="club"):
#         returnpage="shophome.html"
#     elif(request.session.get("role","")=="turf"):
#         returnpage="turfhome.html"
#     return render(request,"privacy.html",{"role":returnpage,"msg":msg})



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


# user
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


def approve_user(request):
    datauser=usr.objects.filter(status="waiting").all()
    return render(request,"approve_user.html",{"data":datauser})
def approved_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).update(status="approved")
    response = redirect("/approve_user")
    return response

def reject_user(request):
    id=request.POST["user_id"]
    loid=request.POST["lo_id"]
    log.objects.filter(logid=loid).delete()
    usr.objects.filter(user_id=id).delete()
    response = redirect("/approve_user")
    return response

def list_user(request):
    datausr=usr.objects.filter(status="approved").all()
    if request.POST:
        t1=request.POST["search_user"]
        datausr=usr.objects.filter(status="approved",username=t1).all()
    return render(request,"list_user.html",{"data":datausr})

def delete_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).delete()
    response = redirect("/list_user")
    return response

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

def guest(request): 
    datashp=turf.objects.filter(status="approved").all()
    return render(request,"guest.html",{"data":datashp})

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
    


def listpack(request):
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
            return redirect('guest')  # Redirect to the same page to avoid form resubmission
            
        return render(request, "listpack.html", {"d": data, "s1": s1, "packages": packages})
    
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


  
#shop 
# def shopreg(request):
#     shop_name=request.POST["shop_name"]
#     shop_address=request.POST["shop_address"]
#     shop_phone=request.POST["shop_phone"]
#     shop_email=request.POST["shop_email"]
#     shop_district=request.POST["district"]
#     did=dist.objects.get(district_id=shop_district)
#     shop_location=request.POST["location"]
#     sid=loc.objects.get(location_id=shop_location)
#     username=request.POST["username"]
#     password=request.POST["password"]
#     log.objects.create(username=username,password=password,role="shop")
#     datal=log.objects.last()
#     shop.objects.create(login=datal,shop_name=shop_name,shop_address=shop_address,shop_phone=shop_phone,shop_email=shop_email,district=did,locations=sid,status="waiting")
#     response = redirect('/index')
#     return response

# def approve_shop(request):
#     datashop=shop.objects.filter(status="waiting").all()
#     return render(request,"approve_shop.html",{"data":datashop})

# def approved_shop(request):
#     id=request.POST["shop_id"]
#     shop.objects.filter(shop_id=id).update(status="approved")
#     response = redirect("/approve_shop")
#     return response

def reject_shop(request):
    id=request.POST["shop_id"]
    shop.objects.filter(shop_id=id).delete()
    response = redirect("/approve_shop")
    return response

# def list_shop(request):
#     datashp=shop.objects.filter(status="approved").all()
#     if request.POST:
#         t1=request.POST["search_shop"]
#         datashp=shop.objects.filter(status="approved",username=t1).all()
#     return render(request,"list_shop.html",{"data":datashp})

# def delete_shop(request):
#     id=request.POST["shop_id"]
#     shop.objects.filter(shop_id=id).delete()
#     response = redirect("/list_shop")
#     return response

# def shopComplaints(request):
#     msg = ""
#     logid = request.session['id']            
#     logdata = shop.objects.get(login=logid)
#     data = scomp.objects.filter(shop_id=logdata)
#     return render(request,"shopComplaints.html",{"msg":msg,"data":data})
    
# def shopAddComplaint(request):
#     if request.POST:
#         logid = request.session['id']
#         logdata = shop.objects.get(login=logid)
#         today = date.today()
#         subject = request.POST['subject']
#         complaint = request.POST['complaint']
#         scomp.objects.create(ssubject=subject,smsg=complaint,scomplaint_date=today,shop_id=logdata)
#     response = redirect('/shopComplaints')
#     return response

def shopProfile(request):
    msg = ""
    logid = request.session['id']
    data = usr.objects.get(login=logid)
    return render(request,"shopProfile.html",{"msg":msg,"data":data})

def shopProfileUpdate(request):
    if request.POST:
        logid = request.session['id']
        shopid = request.POST['turfid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
       

        usr.objects.filter(user_id=shopid).update(user_name=name,user_email=email,user_phone=phone,user_contact=address)
    response = redirect('/shopProfile')
    return response

# def shop_feed(request):
#     if request.POST:
#         t1= request.POST["t1"]
#         t2= request.POST["t2"]
#         scomp.objects.filter(scomplaint_id=t1).update(reply=t2)
#     data=scomp.objects.all()
#     return render(request,"shop_feed.html",{"data":data})

# def shopRegisterItem(request):
#     msg = ""
#     return render(request,"shopRegisterItem.html",{"msg":msg})

# def shopRegisterItemProcess(request):
#     name=request.POST["name"]
#     desc=request.POST["desc"]
#     photo=request.FILES["photo"]
#     logid = request.session['id']
#     logdata = shop.objects.get(login=logid)
#     sitem.objects.create(sitem_name=name,sitem_description=desc,sitem_photo=photo,shop=logdata,sitem_status="waiting")
#     response = redirect('/shopRegisterItem')
#     return response

# def shopItemList(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = shop.objects.get(login=logid)
#     data = sitem.objects.filter(shop=logdata)
#     return render(request,"shopItemList.html",{"msg":msg,"data":data})

# def shopItemUpdate(request):
#     if request.POST:
#         itemid = request.POST['itemid']
#         name = request.POST["pname"]
#         desc = request.POST["pdesc"]
       
#         sitem.objects.filter(sitem_id=itemid).update(sitem_name=name,sitem_description=desc)

#     response = redirect('/shopItemList')
#     return response

# def shopItemDelete(request):
#     if request.POST:
#         itemid = request.POST['itemid']
#         sitem.objects.filter(itemid=itemid).delete()
#     response = redirect('/shopItemList')
#     return response

# def shopRegisterStock(request):
#     msg = ""
#     return render(request,"shopRegisterStock.html",{"msg":msg})

# def shopRegisterStockProcess(request):
#     quantity=request.POST["stock_quantity"]
#     price=request.POST["stock_itemprice"]
#     brand=request.POST["stock_itembrand"]
#     logid = request.session['id']
#     logsdata=shop.objects.get(login=logid)
#     logdata=sitem.objects.get(shop_id=logsdata)
#     stock.objects.create(stock_quantity=quantity,stock_itemprice=price,stock_itembrand=brand,saleitem=logdata,stock_status="waiting")
#     response = redirect('/shopRegisterStock')
#     return response

# def shopStockList(request):
#     msg = ""
#     logid = request.session['id']
#     logsdata = shop.objects.get(login=logid)
#     logdata=sitem.objects.get(shop_id=logsdata)
#     data = stock.objects.filter(saleitem=logdata)
#     return render(request,"shopStockList.html",{"msg":msg,"data":data})

# def shopStockUpdate(request):
#     if request.POST:
#         stockid= request.POST['stockid']
#         quantity = request.POST["stock_quantity"]
#         price = request.POST["stock_itemprice"]
#         brand=request.POST["stock_itembrand"]
#         stock.objects.filter(stock_id=stockid).update(stock_quantity=quantity,stock_itemprice=price,stock_itembrand=brand)

#     response = redirect('/shopStockList')
#     return response

# def shopStockDelete(request):
#     if request.POST:
#         stockid = request.POST['stockid']
#         pack.objects.filter(stockid=stockid).delete()
#     response = redirect('/shopStockList')
#     return response

def itemlist(request):
    data=stock.objects.filter(stock_status="waiting").all()
    return render(request,"allitems.html",{"data":data})
    
#club
# def clubreg(request):
#     club_name=request.POST["club_name"]
#     club_address=request.POST["club_address"]
#     club_phone=request.POST["club_phone"]
#     club_email=request.POST["club_email"]
#     club_banner=request.POST["club_banner"]
#     club_district=request.POST["district"]
#     did=dist.objects.get(district_id=club_district)
#     club_location=request.POST["location"]
#     sid=loc.objects.get(location_id=club_location)
#     username=request.POST["username"]
#     password=request.POST["password"]
#     log.objects.create(username=username,password=password,role="club")
#     datal=log.objects.last()
#     club.objects.create(login=datal,club_name=club_name,club_address=club_address,club_phone=club_phone,club_email=club_email,club_banner=club_banner,district=did,locations=sid,status="waiting")
#     response = redirect('/index')
#     return response

# def approve_club(request):
#     dataclub=club.objects.filter(status="waiting").all()
#     return render(request,"approve_club.html",{"data":dataclub})

# def approved_club(request):
#     id=request.POST["club_id"]
#     club.objects.filter(club_id=id).update(status="approved")
#     response = redirect("/approve_club")
#     return response

# def reject_club(request):
#     id=request.POST["club_id"]
#     club.objects.filter(club_id=id).delete()
#     response = redirect("/approve_club")
#     return response

# def list_club(request):
#     dataclb=club.objects.filter(status="approved").all()
#     if request.POST:
#         t1=request.POST["search_club"]
#         dataclb=club.objects.filter(status="approved",username=t1).all()
#     return render(request,"list_club.html",{"data":dataclb})

# def delete_club(request):
#     id=request.POST["club_id"]
#     club.objects.filter(club_id=id).delete()
#     response = redirect("/list_club")
#     return response

# def clubComplaints(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = club.objects.get(login=logid)
#     data = ccomp.objects.filter(club_id=logdata)
#     return render(request,"clubComplaints.html",{"msg":msg,"data":data})
    
# def clubAddComplaint(request):
#     if request.POST:
#         logid = request.session['id']
#         logdata = club.objects.get(login=logid)
#         today = date.today()
#         subject = request.POST['subject']
#         complaint = request.POST['complaint']
#         ccomp.objects.create(csubject=subject,cmsg=complaint,ccomplaint_date=today,club_id=logdata)
#     response = redirect('/clubComplaints')
#     return response

# def clubPrivacy(request):
#     msg = ""
#     if request.POST:
#         t1=request.POST["cpass"]
#         t2=request.POST["npass"]

#         id=request.session['id']
#         data=log.objects.get(logid=id)
#         if data.password==t1:
#             msg="Password updated"
#             log.objects.filter(logid=id).update(password=t2)
#         else:
#             msg="invalid current password"

#     return render(request,"clubPrivacy.html",{"msg":msg})

# def shopPrivacy(request):
#     msg = ""
#     if request.POST:
#         t1=request.POST["cpass"]
#         t2=request.POST["npass"]

#         id=request.session['id']
#         data=log.objects.get(logid=id)
#         if data.password==t1:
#             msg="Password updated"
#             log.objects.filter(logid=id).update(password=t2)
#         else:
#             msg="invalid current password"

#     return render(request,"shopPrivacy.html",{"msg":msg})

# def club_feed(request):
#     if request.POST:
#         t1= request.POST["t1"]
#         t2= request.POST["t2"]
#         ccomp.objects.filter(ccomplaint_id=t1).update(reply=t2)
#     data=ccomp.objects.all()
#     return render(request,"club_feed.html",{"data":data})   

# def clubRegisterTour(request):
#     msg = ""
#     return render(request,"tournaments.html",{"msg":msg})

# def tournament(request):
#     msg = ""
#     if request.POST:
#         tour_name=request.POST["tour_name"]
#         tour_details=request.POST["tour_details"]
#         tour_venue=request.POST["tour_venue"]
#         tour_date=date.today()
#         tour_time=time.time()
#         ticketcharge=request.POST["ticketcharge"]
#         no_tickets=request.POST["no_tickets"]
#         logid = request.session['id']
#         logdata = club.objects.get(login=logid)
#         tour.objects.create(tour_name=tour_name,tour_details=tour_details,tour_venue=tour_venue,tour_date=tour_date,tour_time=tour_time,ticketcharge=ticketcharge,no_tickets=no_tickets,club=logdata,tour_status="waiting")
#     response = redirect('/clubRegisterTour')
#     return response

# def clubProfile(request):
#     msg = ""
#     logid = request.session['id']
#     data = club.objects.get(login=logid)
#     return render(request,"clubprofile.html",{"msg":msg,"data":data})  

# def clubProfileUpdate(request):
#     if request.POST:
#         logid = request.session['id']
#         club_id = request.POST['club_id']
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         address = request.POST['address']
       

#         club.objects.filter(club_id=club_id).update(club_name=name,club_email=email,club_phone=phone,club_address=address)
#     response = redirect('/clubProfile')
#     return response

# def clubTourList(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = club.objects.get(login=logid)
#     data = tour.objects.filter(club=logdata)
#     return render(request,"clubTourList.html",{"msg":msg,"data":data})

# def clubTourUpdate(request):
#     if request.POST:
#         tour_id = request.POST['tour_id']
#         name = request.POST["pname"]
#         details = request.POST["pdesc"]
       
#         tour.objects.filter(tour_id=tour_id).update(tour_name=name,tour_details=details)

#     response = redirect('/clubTourList')
#     return response

# def clubTourDelete(request):
#     if request.POST:
#         tour_id = request.POST['tour_id']
#         tour.objects.filter(tour_id=tour_id).delete()
#     response = redirect('/clubTourList')
#     return response

# def approve_tour(request):
#     datatour=tour.objects.filter(tour_status="waiting").all()
#     return render(request,"clubTourList.html",{"data":datatour})

# def approved_tour(request):
#     id=request.POST["tour_id"]
#     tour.objects.filter(tour_id=id).update(tour_status="approved")
#     response = redirect("/clubTourList")
#     return response

# def tour_approve(request):
#     datatour=tour.objects.filter(tour_status="approved").all()
#     return render(request,"tour_approval.html",{"data":datatour})

# def tour_approval(request):
#     id=request.POST["tourid"]
#     tour.objects.filter(tour_id=id).update(tour_status="accepted")
#     response = redirect("/tour_approve")
#     return response

# def approved_tournament(request):
#     datatour=tour.objects.filter(tour_status="accepted").all()
#     return render(request,"clubApprovedtourlist.html",{"data":datatour})

#turf
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
    turf.objects.create(login=datal,turf_name=turf_name,turf_address=turf_address,turf_phone=turf_phone,turf_email=turf_email,district=did,locations=sid,status="waiting")
    response = redirect('/index')
    return response

def approve_turf(request):
    dataturf=turf.objects.filter(status="waiting").all()
    return render(request,"approve_turf.html",{"data":dataturf})

def approved_turf(request):
    id=request.POST["turf_id"]
    lid=request.POST["lo_id"]
    log.objects.filter(logid=lid).update(role="turf")
    turf.objects.filter(turf_id=id).update(status="approved")
    response = redirect("/approve_turf")
    return response

def reject_turf(request):
    id=request.POST["turf_id"]
    lid=request.POST["lo_id"]
    log.objects.filter(logid=lid).delete()
    turf.objects.filter(turf_id=id).delete()
    response = redirect("/approve_turf")
    return response

def list_turf(request):
    datatrf=turf.objects.filter(status="approved").all()
    if request.POST:
        t1=request.POST["search_turf"]
        datatrf=turf.objects.filter(status="approved",username=t1).all()
    return render(request,"list_turf.html",{"data":datatrf})

def delete_turf(request):
    id=request.POST["turf_id"]
    turf.objects.filter(turf_id=id).delete()
    response = redirect("/list_turf")
    return response

def turf_feed(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        tcomp.objects.filter(tcomplaint_id=t1).update(creply=t2)
    data=tcomp.objects.all()
    return render(request,"turf_feed.html",{"data":data})

# Create your views here.


################################# ABHISHEK #######################################

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
    logdata = turf.objects.get(login=logid)
    pack.objects.create(pack_name=name,pack_rate=rate,pack_type=type,pack_image=photo,pack_turf=logdata,pack_status="waiting")
    response = redirect('/turfRegisterPackage')
    return response

def turfPackageList(request):
    msg = ""
    logid = request.session['id']
    logdata = turf.objects.get(login=logid)
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
    logdata = turf.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="waiting")
    return render(request,"turfPackageNewBookings.html",{"msg":msg,"data":data})

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
    logdata = turf.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="approved")
    return render(request,"turfPackageApprovedBookings.html",{"msg":msg,"data":data})

def turfPackageRescheduleRequests(request):
    msg = ""
    logid = request.session['id']
    logdata = turf.objects.get(login=logid)
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
    logdata = turf.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="confirm")
    return render(request,"turfPackageRescheduledBookings.html",{"msg":msg,"data":data})
    
def turfPackageCancelledBookings(request):
    msg = ""
    logid = request.session['id']
    logdata = turf.objects.get(login=logid)
    data = pbook.objects.filter(turf=logdata,status="cancelled")
    return render(request,"turfPackageCancelledBookings.html",{"msg":msg,"data":data})
    
def turfComplaints(request):
    msg = ""
    logid = request.session['id']
    logdata = turf.objects.get(login=logid)
    data = tcomp.objects.filter(turf=logdata)
    return render(request,"turfComplaints.html",{"msg":msg,"data":data})
    
def turfAddComplaint(request):
    if request.POST:
        logid = request.session['id']
        logdata = turf.objects.get(login=logid)
        today = date.today()

        subject = request.POST['subject']
        complaint = request.POST['complaint']
        tcomp.objects.create(tsubject=subject,tmsg=complaint,tcomplaint_date=today,turf_id=logdata.turf_id)
    response = redirect('/turfComplaints')
    return response
    
def turfProfile(request):
    msg = ""
    logid = request.session['id']
    data = turf.objects.get(login=logid)
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

        turf.objects.filter(turf_id=turfid).update(turf_name=name,turf_email=email,turf_phone=phone,turf_address=address,turf_ownername=owner,turf_squarefeet=size)
    response = redirect('/turfProfile')
    return response

# def turfAddItems(request):
#     msg=""
#     return render(request,"turfAddItems.html",{"msg":msg})

# def turfAddItemsProcess(request):
    
#     if request.POST:
#         logid = request.session['id']
#         logdata = turf.objects.get(login=logid)
#         name = request.POST['name']
#         rate = request.POST['rate']
#         photo = request.FILES['photo']
#         ritem.objects.create(item_name=name,item_image=photo,item_rph=rate,rent_turf_id=logdata,item_status="waiting")
#     response = redirect('/turfAddItems')
#     return response

# def turfRentItems(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = turf.objects.get(login=logid)
#     data = ritem.objects.filter(rent_turf=logdata)
#     return render(request,"turfRentItems.html",{"msg":msg,"data":data})

# def turfRentItemUpdate(request):
#     msg = ""
#     if request.POST:
#         rentid = request.POST['rentid']
#         name = request.POST['iname']
#         rate = request.POST['irate']

#         ritem.objects.filter(rentid=rentid).update(item_name=name,item_rph=rate)
#     response = redirect('/turfRentItems')
#     return response

# def turfRentItemDelete(request):
#     msg = ""
#     if request.POST:
#         rentid = request.POST['rentid']
#         ritem.objects.filter(rentid=rentid).delete()
        
#     response = redirect('/turfRentItems')
#     return response

# def turfRentItemNewBookings(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = turf.objects.get(login=logid)
#     data = rbook.objects.filter(turf=logdata,book_status="waiting")
#     return render(request,"turfRentItemNewBookings.html",{"msg":msg,"data":data})

# def turfRentItemBookingApprove(request):
#     msg = ""
#     if request.POST:
#         rbookid = request.POST['rbookid']

#         rbook.objects.filter(rbookid=rbookid).update(book_status="approved")
#     response = redirect('/turfRentItemNewBookings')
#     return response

# def turfRentItemBookingReject(request):
#     msg = ""
#     if request.POST:
#         rbookid = request.POST['rbookid']

#         rbook.objects.filter(rbookid=rbookid).update(book_status="rejected")
#     response = redirect('/turfRentItemNewBookings')
#     return response

# def turfRentItemApprovedBookings(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = turf.objects.get(login=logid)
#     data = rbook.objects.filter(turf=logdata,book_status="approved")
#     return render(request,"turfRentItemApprovedBookings.html",{"msg":msg,"data":data})

# def turfRentItemRejectedBookings(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = turf.objects.get(login=logid)
#     data = rbook.objects.filter(turf=logdata,book_status="rejected")
#     return render(request,"turfRentItemRejectedBookings.html",{"msg":msg,"data":data})

# def turfRentItemCancelledBookings(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = turf.objects.get(login=logid)
#     data = rbook.objects.filter(turf=logdata,book_status="cancelled")
#     return render(request,"turfRentItemCancelledBookings.html",{"msg":msg,"data":data})

# def turfRentItemBookingRefund(request):
#     msg = ""
#     if request.POST:
#         rbookid = request.POST['rbookid']

#         rbook.objects.filter(rbookid=rbookid).update(pay_status="refunded")
#     response = redirect('/turfRentItemCancelledBookings')
#     return response

def cart(request):
    return render(request,"cart.html")  

def clubRegisterTicket(request):
    msg = ""
    return render(request,"tickets.html",{"msg":msg})

def ticket(request):
    msg="Successfully Updated"
    if request.POST:
        bookdate=request.POST["bookdate"]
        ticketcount=request.POST["ticketcount"]
        logid = request.session['id']
        logdata = club.objects.get(login=logid)
        tbook.objects.create(club=logdata,bookdate=bookdate,ticketcount=ticketcount,ticket_status="waiting")
        msg="Successfully Updated"
    else:
        msg=""
    data1=tbook.objects.all()
    return render(request,"tickets.html",{"msg":msg,"data":data1})
    
def clubTicketList(request):
    msg = ""
    logid = request.session['id']
    logdata = club.objects.get(login=logid)
    data = tbook.objects.filter(club=logdata)
    return render(request,"clubTicketList.html",{"msg":msg,"data":data})

# def newOrderBookings(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = shop.objects.get(login=logid)
#     data = ord.objects.filter(shop = logdata).all()
#     return render(request,"orderItemListed.html",{"msg":msg,"data":data})

# def newOrderBookinApprove(request):
#     msg = ""
#     if request.POST:
#         order_id = request.POST['order_id']
#         ord.objects.filter(order_id=order_id).update(order_status="completed")
#     response = redirect('/newOrderBookings')
#     return response

# def shopItemPaidBookings(request):
#     msg = ""
#     logid = request.session['id']
#     logdata = shop.objects.get(login=logid)
#     data = ord.objects.filter(shop=logdata,order_status="completed")
#     return render(request,"shopItemPaidBookings.html",{"msg":msg,"data":data})

#def turfRentItemCancelledBookings(request):
    #msg = ""
    #logid = request.session['id']
    #logdata = ords.objects.get(login=logid)
    #data = orditem.objects.filter(order=logdata,order_status="approved")
    #return render(request,"shopItemApprovedBookings.html",{"msg":msg,"data":data})









##################################################################
###################### Android Api ###############################
##################################################################

# from django.http import HttpResponse,JsonResponse
# import json

# def app_login(request):
#     t1=request.POST["t1"]
#     t2=request.POST["t2"]
#     msg="try again later"
#     c=log.objects.filter(username=t1,password=t2).count()
#     if c == 1 : 
#         dat=log.objects.get(username=t1,password=t2)
#         if(dat.role == "user"):
#             du=usr.objects.get(login=dat)
#             if du.status == "waiting":
#                 msg="not yet verified"
#             else :
#                 msg="ok:"+str(dat.logid)+":user:"+du.user_name+":"+str(du.district.district_id)+":"+str(du.locations.location_id)
#         else:
#             msg="invalid account Details"
#     else:
#          msg="invalid user name or password"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)

# def app_register(request):
#     t1=request.POST["t1"]
#     t2=request.POST["t2"]
#     t3=request.POST["t3"]
#     t4=request.POST["t4"]
#     t5=request.POST["t5"]
#     t6=request.POST["t6"]
#     t7=request.POST["t7"]

#     dst = dist.objects.get(district_id=t4)
#     loca = loc.objects.get(location_id=t5)

#     log.objects.create(username=t6,password=t7,role="user")
#     data=log.objects.last()
#     usr.objects.create(user_name=t1,user_phone=t2,user_email=t3,district=dst,locations=loca, status="waiting",login=data)
#     msg="ok:"+str(data.logid)
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)

# def app_getdistrict(request):

#     datar=dist.objects.values("district_id","district")
#     data=json.dumps(list(datar))
#     return HttpResponse(data, content_type="application/json")

# def app_getlocation(request):
#     t1 = request.POST["t1"]
#     datax=dist.objects.get(district_id=t1)
#     datar=loc.objects.filter(district=datax).values("location_id","location")
#     data=json.dumps(list(datar))
#     return HttpResponse(data, content_type="application/json")

# def app_getUserProfile(request):
#     user = usr.objects.filter(login = request.POST['t1']).values("user_id","user_name","user_phone","user_email")
#     data=json.dumps(list(user))
    
#     return HttpResponse(data, content_type="application/json")

# def app_changePassword(request):
#     t1=request.POST["t1"]
#     t2=request.POST["t2"]
#     t3=request.POST["t3"]
#     data=log.objects.get(logid = t3)
#     if data.password == t1:
#         msg="ok"
#         log.objects.filter(logid = t3).update(password = t2)
#     else:
#         msg="invalid current password"
    
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)

# def app_getTurfList(request):
#     t1 = request.POST["t1"]
#     datax=dist.objects.get(district_id=t1)
#     datar = turf.objects.filter(district=t1).all()
    
#     db = []
#     for d in datar:
        
#         v = {
#             "turf_id":str(d.turf_id),
#             "turf_name":d.turf_name,
#             "turf_phone":d.turf_phone,
#             "turf_email":d.turf_email,
#             "turf_address":d.turf_address,
#             "turf_squarefeet":d.turf_squarefeet,
#             "turf_ownername":d.turf_ownername,
#             "district_id":str(d.district),
#             "district":str(d.district.district),
#             "locations_id":str(d.locations),
#             "location":str(d.locations.location)
#         }
#         db.append(v)

#     data=json.dumps(list(db))
#     return HttpResponse(data, content_type="application/json")

# def app_getTurfPackages(request):
#     t1 = request.POST["t1"]
#     datar = pack.objects.filter(pack_turf = t1, pack_status = "approved").values("packid","pack_name","pack_rate","pack_type","pack_status","pack_image","pack_turf_id")
#     data=json.dumps(list(datar))
    
#     return HttpResponse(data, content_type="application/json")

# def app_bookPackage(request):
#     t1 = request.POST["t1"] #date
#     t2 = pack.objects.get(packid = request.POST["t2"])
#     t3 = turf.objects.get(turf_id = request.POST["t3"])
#     t4 = usr.objects.get(login = request.POST["t4"])

#     pbook.objects.create(date = t1, status = "waiting", package = t2, turf = t3 ,user = t4)
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)

# def app_getPackageBookings(request):
#     t1 = usr.objects.get(login = request.POST["t1"]) #date

#     datar = pbook.objects.filter(user = t1).all()
    
#     db = []
#     for d in datar:
        
#         v = {
#             "pbookid":str(d.pbookid),
#             "date":d.date,
#             "status":d.status,
#             "package_id":str(d.package),
#             "turf_id":str(d.turf),
#             "turf_name":str(d.turf.turf_name),
#             "user_id":str(d.user),
#             "pack_name":str(d.package.pack_name),
#             "pack_type":str(d.package.pack_type),
#             "pack_rate":str(d.package.pack_rate),
#             "pack_status":str(d.package.pack_status),
#             "pack_image":str(d.package.pack_image)
#         }
#         db.append(v)

#     data=json.dumps(list(db))
#     return HttpResponse(data, content_type="application/json")

# def app_rescheduleBooking(request):
#     t1 = request.POST["t1"] #pbookid
#     t2 = request.POST["t2"] #date
#     pbook.objects.filter(pbookid = t1).update(date = t2, status = "reschedule")
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)

# def app_cancelTurfBooking(request):
#     t1 = request.POST["t1"] #pbookid
#     pbook.objects.filter(pbookid = t1).update(status = "cancelled")
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)
    
# def app_getRentItems(request):
#     t1 = request.POST["t1"] #turfid
#     datar = ritem.objects.filter(rent_turf = t1, item_status = "approved").values("rentid","item_name","item_image","item_rph","item_status","rent_turf_id")
#     data=json.dumps(list(datar))
    
#     return HttpResponse(data, content_type="application/json")
    
# def app_bookRentItem(request):
#     t1 = ritem.objects.get(rentid = request.POST["t1"]) #rentitem
#     t2 = usr.objects.get(login = request.POST["t2"]) #logid
#     t3 = request.POST["t3"] #bdate
#     t4 = request.POST["t4"] #btime
#     t5 = turf.objects.get(turf_id = request.POST["t5"]) #turf
#     rbook.objects.create(rent_item = t1, turf = t5, rent_hours = t4, rbook_date = t3 ,rent_user = t2, book_status = "waiting", pay_status = "waiting")
    
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)
    
# def app_getRentItemBookings(request):
#     t1 = usr.objects.get(login = request.POST["t1"]) #date

#     datar = rbook.objects.filter(rent_user = t1).all()
    
#     db = []
#     for d in datar:
        
#         v = {
#             "rbookid":str(d.rbookid),
#             "rent_hours":d.rent_hours,
#             "rbook_date":d.rbook_date,
#             "book_status":str(d.book_status),
#             "pay_status":str(d.pay_status),
#             "rent_item_id":str(d.rent_item),
#             "item_name":str(d.rent_item.item_name),
#             "item_image":str(d.rent_item.item_image),
#             "item_rph":str(d.rent_item.item_rph),
#             "rent_user_id":str(d.rent_user),
#             "turf_id":str(d.turf),
#             "turf_name":str(d.turf.turf_name)
#         }
#         db.append(v)

#     data=json.dumps(list(db))
#     return HttpResponse(data, content_type="application/json")
    
# def app_cancelItemBooking(request):
#     t1 = request.POST["t1"] #rbookid
#     rbook.objects.filter(rbookid = t1).update(book_status = "cancelled")
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)
    
# def app_getTournament(request):
#     today = date.today()
#     #valid_until may be empty
#     # profile = Profile.objects.filter(company=request.user.company).filter(Q(tour_date__gte=today))
#     datar = tour.objects.filter(Q(tour_date__gte=today)).all()
    
#     db = []
#     for d in datar:
        
#         v = {
#             "tour_id":str(d.tour_id),
#             "tour_name":d.tour_name,
#             "tour_details":d.tour_details,
#             "tour_venue":str(d.tour_venue),
#             "tour_time":str(d.tour_time),
#             "tour_date":str(d.tour_date),
#             "ticketcharge":str(d.ticketcharge),
#             "no_tickets":str(d.no_tickets),
#             "tour_status":str(d.tour_status),
#             "soldcount":str(d.soldcount),
#             "club_id":str(d.club),
#             "club_name":str(d.club.club_name),
#             "club_phone":str(d.club.club_phone)
#         }
#         db.append(v)

#     data=json.dumps(list(db))
#     return HttpResponse(data, content_type="application/json")
    
# def app_bookTicket(request):
#     t1 = usr.objects.get(login = request.POST['t1'])
#     t2 = request.POST['t2']
#     t3 = tour.objects.get(tour_id = request.POST['t3'])
#     today = date.today()

#     tbook.objects.create(bookdate = today, ticketcount = t2, ticket_status = "waiting", tour = t3, user = t1)
#     new = int(t3.no_tickets)-int(t2)
#     tour.objects.filter(tour_id = t3.tour_id).update(no_tickets = new)

#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)
    
# def app_getBookedTickets(request):
#     t1 = usr.objects.get(login = request.POST['t1'])
#     print(t1)
#     datar = tbook.objects.filter(user = t1).all()
    
#     db = []
#     for d in datar:
        
#         v = {
#             "booking_id":str(d.booking_id),
#             "bookdate":d.bookdate,
#             "ticketcount":d.ticketcount,
#             "ticket_status":str(d.ticket_status),
#             "tour_id":str(d.tour),
#             "tour_name":str(d.tour.tour_name),
#             "tour_details":str(d.tour.tour_details),
#             "tour_venue":str(d.tour.tour_venue),
#             "tour_time":str(d.tour.tour_time),
#             "tour_date":str(d.tour.tour_date),
#             "ticketcharge":str(d.tour.ticketcharge),
#             "user_id":str(d.user_id),
#             "today": str(date.today())
#         }
#         db.append(v)

#     data=json.dumps(list(db))
#     return HttpResponse(data, content_type="application/json")

# def app_getShopList(request):
#     t1 = request.POST["t1"] #dist
#     datar = shop.objects.filter(district = t1, status = "approved").values("shop_id","shop_name","shop_phone","shop_email","shop_address","status")
#     data=json.dumps(list(datar))
    
#     return HttpResponse(data, content_type="application/json")

# def app_getShopProducts(request):
#     t1 = shop.objects.get(shop_id = request.POST['t1'])
#     print(t1)
#     datar = sitem.objects.filter(shop = t1).all()
    
#     db = []
#     for d in datar:
        
#         v = {
#             "sitem_id":str(d.sitem_id),
#             "sitem_name":d.sitem_name,
#             "sitem_photo":str(d.sitem_photo),
#             "sitem_description":str(d.sitem_description),
#             "sitem_price":str(d.sitem_price),
#             "sitem_stock":str(d.sitem_stock),
#             "shop_id":str(d.shop),
#             "shop_name":str(d.shop.shop_name),
#             "shop_phone":str(d.shop.shop_phone),
#             "sitem_status":str(d.sitem_status)
#         }
#         db.append(v)

#     data=json.dumps(list(db))
#     return HttpResponse(data, content_type="application/json")

# def app_bookProduct(request):
#     t1=usr.objects.get(login = request.POST["t1"]) #log
#     t2=request.POST["t2"] #qty
#     t3=sitem.objects.get(sitem_id = request.POST["t3"]) #item
#     shopid = shop.objects.get(shop_id = t3.shop.shop_id)
#     today = date.today()

#     current = ord.objects.filter(order_status="waiting",user=t1).count()
#     if(current==0):
#         ord.objects.create(user=t1,order_status="waiting",shop = shopid)
#         id = ord.objects.last()
#     else:
#         id = ord.objects.get(order_status="waiting",user=t1,shop = shopid)

#     orditem.objects.create(quantity=t2,item=t3,order=id)
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)
    
# def app_getCartItems(request):
#     t1 = request.POST["t1"]
#     d1 = usr.objects.get(login=t1)

#     ordercount = ord.objects.filter(user=d1,order_status="waiting").count()
#     data = []
#     if(ordercount > 0):
#         corder = ord.objects.filter(user=d1,order_status="waiting").all()
#         for c in corder:
#             dataw = orditem.objects.filter(order = c.order_id).all()

#             for d in dataw:
#                 dv = {
#                     "order_itemid":str(d.order_itemid),
#                     "quantity":str(d.quantity),
#                     "item_id":str(d.item),
#                     "sitem_name":d.item.sitem_name,
#                     "sitem_photo":str(d.item.sitem_photo),
#                     "sitem_description":str(d.item.sitem_description),
#                     "sitem_price":d.item.sitem_price,
#                     "sitem_stock":d.item.sitem_stock,
#                     "shop_id":str(d.item.shop),
#                     "order_id":str(d.order),
#                     "order_status":str(d.order.order_status)
#                 }
#                 data.append(dv)
    
#     return JsonResponse(data, safe=False)

# def app_PlaceOrder(request):
#     t1 = request.POST["t1"]
#     log = usr.objects.get(login = t1)
    
#     d1 = ord.objects.filter(user=log,order_status="waiting").all()
#     for da in d1:
#         ord.objects.filter(order_id=da.order_id).update(order_status="paid")
#         d2 = orditem.objects.filter(order=da.order_id).all()
#         for db in d2:
#             sitem.objects.filter(sitem_id=db.item.sitem_id).update(sitem_stock=int(db.item.sitem_stock)-int(db.quantity))
#     msg="ok"
#     data=[{'result': msg}]
#     return JsonResponse(data, safe=False)

# def app_getOrderHistory(request):
#     t1 = request.POST["t1"]
#     d1 = usr.objects.get(login=t1)

#     ordercount = ord.objects.filter(~Q(order_status="waiting"),user=d1).count()
#     data = []
#     if(ordercount > 0):
#         corder = ord.objects.filter(~Q(order_status="waiting"),user=d1).all()
#         for c in corder:
#             dataw = orditem.objects.filter(order = c.order_id).all()

#             for d in dataw:
#                 dv = {
#                     "order_itemid":str(d.order_itemid),
#                     "quantity":str(d.quantity),
#                     "item_id":str(d.item),
#                     "sitem_name":d.item.sitem_name,
#                     "sitem_photo":str(d.item.sitem_photo),
#                     "sitem_description":str(d.item.sitem_description),
#                     "sitem_price":d.item.sitem_price,
#                     "sitem_stock":d.item.sitem_stock,
#                     "shop_id":str(d.item.shop),
#                     "order_id":str(d.order),
#                     "order_status":str(d.order.order_status)
#                 }
#                 data.append(dv)
    
#     return JsonResponse(data, safe=False)