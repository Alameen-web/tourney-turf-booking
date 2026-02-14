from django.shortcuts import render, redirect
from tapp.models import login as log, user as usr, turf


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

# Admin User Validations
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
# Admin Turf Validations
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
