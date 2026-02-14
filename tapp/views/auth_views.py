from django.shortcuts import render, redirect
from tapp.models import login as log

def adlogin(request):
    return render(request,"adminlog.html")

def userlog(request):
    return render(request,"userlog.html")
 
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
                else:
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
