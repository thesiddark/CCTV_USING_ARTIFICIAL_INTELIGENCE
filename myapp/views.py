from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect

from myapp.models import *

def admin_home(request):
    return render(request,'ADMIN/Admin_index.html')


def login(request):
    return render(request,'loginindex.html')

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    abc=Login.objects.filter( username=username,password=password)
    if abc.exists():
        abcd = Login.objects.get(username=username, password=password)
        request.session["lid"]=abcd.id
        if abcd.type == 'admin':
            return HttpResponse('''<script>alert("Welcome Admin Home");window.location='/myapp/homepage/'</script>''')
        elif abcd.type == 'police':
            return HttpResponse('''<script>alert("Welcome Police Home");window.location='/myapp/policehome/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'loginindex.html', {'error_message': "Invalid username or password. Please try again."})


def logout(request):
    request.session['lid']=''
    return render(request, 'loginindex.html', {'logout_message': "You signed out of you account"})


def admin_add_police(request):

    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted");window.location='/myapp/login/'</script>''')

    return render(request,'ADMIN/admin add police.html')

def admin_add_police_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    stationname=request.POST['station name']
    siname=request.POST['siname']
    place=request.POST['PLACE']
    post=request.POST['post']
    pin=request.POST['pin']
    emailid=request.POST['email id']
    phone=request.POST['phone']
    district= request.POST['district']


    log=Login()
    log.username=emailid
    log.password=phone
    log.type='police'
    log.save()

    pol=Police_Station()
    pol.station_name=stationname
    pol.SI_name=siname
    pol.place=place
    pol.post=post
    pol.pin=pin
    pol.email_id=emailid
    pol.district=district
    pol.phone=phone
    pol.LOGIN=log
    pol.save()

    return HttpResponse('''<script>alert("Police Added");window.location="/myapp/homepage/"</script>''')

def admin_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')
    return render(request,'ADMIN/admin change password.html')

def admin_change_password_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    currentpassword = request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']

    abc=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if abc.exists():
        if newpassword==confirmpassword:
            abc = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("success");window.location='/myapp/login/'</script>''')
        else:
            return render(request, '/ADMIN/admin change password.html',
                          {'pass_message': "something went wrong (Error:01)"})
    else:
        return render(request, 'ADMIN/admin change password.html',
                      {'pass_message': "Please check your Current password (Error:02)"})



def admin_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var = Complaints.objects.all()
    return render(request,'ADMIN/admin complaints.html',{'data':var})

def admin_complaints_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    fromdate=request.POST['from']
    todate = request.POST['to']
    var = Complaints.objects.filter(date__range=[fromdate,todate])
    return render(request, 'ADMIN/admin complaints.html', {'data': var})



def send_reply(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    return render(request, "admin/send reply.html", {'id': id})
def send_reply_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    reply = request.POST['reply']
    id = request.POST['cid']
    res = Complaints.objects.filter(id=id).update(reply=reply, status="replied")
    return HttpResponse(        '''<script>alert("sending");window.location='/myapp/complaints/'</script>''')

def admin_edit_police(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    res=Police_Station.objects.get(id=id)
    return render(request,'ADMIN/admin edit police.html',{'data':res})

def admin_edit_police_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    stationname=request.POST['station']
    siname = request.POST['siname']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phone= request.POST['phone']
    district = request.POST['district']
    emailid = request.POST['email_id']
    id=request.POST['id']

    obj=Police_Station.objects.get(id=id)
    obj.station_name=stationname
    obj.SI_name=siname
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.email_id=emailid
    obj.district=district
    obj.phone=phone
    obj.save()

    lb=Login()
    lb.username=emailid
    lb.save()
    return HttpResponse('''<script>alert("edited");window.location='/myapp/view_police/'</script>''')

def admin_suspicious_activity(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logouted");window.location='/myapp/login/'</script>''')

    var = SuspiciousActivities.objects.all()
    return render(request,'ADMIN/admin suspicious activity.html',{'data':var})

def admin_suspicious_activity_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    fromdate = request.POST['from']
    todate = request.POST['to']
    var = SuspiciousActivities.objects.filter(date__range=[fromdate,todate])
    return render(request, 'ADMIN/admin suspicious activity.html', {'data': var})


def admin_view_appreviews(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var = review.objects.all()
    return render(request,'ADMIN/admin view AppReviews.html',{'data':var})

def admin_view_appreviews_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    fromdate = request.POST['from']
    todate = request.POST['to']
    var = review.objects.filter(date__range=[fromdate,todate])
    return render(request, 'ADMIN/admin view AppReviews.html', {'data': var})


def admin_view_criminals(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var = Criminals.objects.all()
    return render(request,'ADMIN/admin view criminals.html',{'data':var})

def admin_view_criminals_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    search=request.POST['textfield']
    var = Criminals.objects.filter(name__icontains=search)
    return render(request, 'ADMIN/admin view criminals.html',{'data':var})

def admin_view_police(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var=Police_Station.objects.all()
    return render(request,'ADMIN/admin view police.html',{'data':var})

def admin_view_police_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    search = request.POST['name']
    var = Police_Station.objects.filter(station_name__icontains=search)
    return render(request, 'ADMIN/admin view police.html', {'data': var})

def admin_delete_police(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    data=Police_Station.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/view_police/"</script>''')


def admin_view_registered_users(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var = User.objects.all()
    return render(request,'ADMIN/admin view registered users.html',{'data':var})

def admin_view_registered_users_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    search = request.POST['name']
    var = User.objects.filter(name__icontains=search)
    return render(request, 'ADMIN/admin view registered users.html',{'data': var})


#police



def police_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')
    return render(request,'POLICE/police change password.html')

def police_change_password_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    currentpassword = request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']

    abc=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if abc.exists():
        if newpassword==confirmpassword:
            abc = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("success");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/myapp/police_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid");window.location='/myapp/police_change_password/'</script>''')



def police_view_profile(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    res=Police_Station.objects.get(LOGIN=request.session['lid'])
    return render(request,"POLICE/view profile.html",{'data':res})


def police_add_criminals(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')
    return render(request,'police/police add criminals.html')

def police_add_criminals_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    pin = request.POST['pin']
    gender = request.POST['gender']
    photo = request.FILES['photo']
    photo1 = request.FILES['photo1']
    photo2= request.FILES['photo2']
    details = request.POST['details']


    from datetime import datetime
    date='p1'+datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs=FileSystemStorage()
    fs.save(date,photo)
    path=fs.url(date)

    from datetime import datetime
    date1 = 'p2'+datetime.now().strftime('%Y%m%d-%H%M%S') + "2.jpg"
    fs1 = FileSystemStorage()
    fs1.save(date1,photo1)
    path1 = fs1.url(date1)


    from datetime import datetime
    date2 = 'p3'+datetime.now().strftime('%Y%m%d-%H%M%S') + "3.jpg"
    fs2 = FileSystemStorage()
    fs2.save(date2,photo2)
    path2 = fs2.url(date2)


    obj=Criminals()
    obj.place=place
    obj.name=name
    obj.pin=pin
    obj.details=details
    obj.district=district
    obj.post=post
    obj.gender=gender
    obj.photo=path
    obj.photo1=path1
    obj.photo2=path2
    obj.POLICE=Police_Station.objects.get(LOGIN=request.session['lid'])
    obj.save()



    return HttpResponse('''<script>alert("Success");window.location="/myapp/policehome/"</script>''')

def police_view_criminals(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')
    res=Criminals.objects.filter(POLICE__LOGIN_id=request.session['lid'])
    return render(request,'police/police view criminals.html',{'data':res})

def police_view_criminals_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    name = request.POST['name']
    res = Criminals.objects.filter(POLICE__LOGIN_id=request.session['lid'],name__icontains=name)
    return render(request, 'police/police view criminals.html', {'data': res})


def policehome(request):

    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    return render(request,'POLICE/Police_index.html')


def police_delete_criminal(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    data=Criminals.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/police_view_criminals/"</script>''')


def police_edit_criminals(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    res=Criminals.objects.get(id=id)
    return render(request,'police/police edit criminals.html',{'data':res})

def police_edit_criminals_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    pin = request.POST['pin']
    gender = request.POST['gender']
    details = request.POST['details']
    id = request.POST['id']

    obj=Criminals.objects.get(id=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        from datetime import datetime
        date = 'p1' + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path
        obj.save()





    if 'photo1' in request.FILES:
        photo1 = request.FILES['photo1']

        from datetime import datetime
        date1 = 'p2' + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs1 = FileSystemStorage()
        fs1.save(date1, photo1)
        path1 = fs1.url(date1)
        obj.photo1=path1
        obj.save()

    if 'photo2' in request.FILES:
        photo2 = request.FILES['photo2']

        from datetime import datetime
        date2 = 'p3' + datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs2 = FileSystemStorage()
        fs2.save(date2, photo2)
        path2 = fs2.url(date2)

        obj.photo2=path2
        obj.save()


    obj.place=place
    obj.name=name
    obj.pin=pin
    obj.details=details
    obj.district=district
    obj.post=post
    obj.gender=gender
    obj.save()



    return HttpResponse('''<script>alert("Updated");window.location="/myapp/police_view_criminals/"</script>''')


def police_view_registered_users(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var = User.objects.all()
    return render(request,'POLICE/police view registered users.html',{'data':var})

def police_view_registered_users_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    search = request.POST['name']
    var = User.objects.filter(name__icontains=search)
    return render(request, 'POLICE/police view registered users.html',{'data': var})

def police_add_suspicious_activity(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    res=Criminals.objects.filter(POLICE__LOGIN_id=request.session['lid'])
    return render(request,'POLICE/police add suspiciousactivity.html',{'data':res})

def police_add_suspicious_activity_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    dates=request.POST['date']
    time=request.POST['time']
    criminal=request.POST['cr']
    place=request.POST['place']
    activity=request.POST['activity']
    photo=request.FILES['photo']

    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    obj=SuspiciousActivities()
    obj.date=dates
    obj.time=time
    obj.activity=activity
    obj.CRIMINAL_id=criminal
    obj.photo=path
    obj.place=place
    obj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/policehome/"</script>''')

def police_suspicious_activity(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    var = SuspiciousActivities.objects.filter(CRIMINAL__POLICE__LOGIN_id=request.session['lid'])
    return render(request,'POLICE/police suspicious activity.html',{'data':var})

def police_suspicious_activity_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    fromdate = request.POST['from']
    todate = request.POST['to']
    var = SuspiciousActivities.objects.filter(CRIMINAL__POLICE__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
    return render(request,'POLICE/police suspicious activity.html',{'data':var})

def police_delete_suspicious(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    data=SuspiciousActivities.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/police_suspicious_activity/"</script>''')



def police_edit_suspicious_activity(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    res2=SuspiciousActivities.objects.get(id=id)
    res=Criminals.objects.filter(POLICE__LOGIN_id=request.session['lid'])
    return render(request,'POLICE/police edit suspiciousactivity.html',{'data':res,'data2':res2})

def police_edit_suspicious_activity_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("logout....");window.location='/myapp/login/'</script>''')

    dates=request.POST['date']
    time=request.POST['time']
    criminal=request.POST['cr']
    place=request.POST['place']
    activity=request.POST['activity']
    id=request.POST['id']


    obj=SuspiciousActivities.objects.get(id=id)
    if 'photo' in  request.FILES:
        photo = request.FILES['photo']

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path

        obj.save()

    obj.date=dates
    obj.time=time
    obj.activity=activity
    obj.CRIMINAL_id=criminal
    obj.place=place
    obj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/police_suspicious_activity/"</script>''')




###########chat


def chat1(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "POLICE/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})

def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})




def User_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    print(FROM_id)
    print(TOID_id)
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})


def User_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.FROMID_id, "date": i.date, "to": i.TOID_id})

    return JsonResponse({"status":"ok",'data':l})

# users

# def user_add_family_members(request):
#     return render(request, 'user/user add family members.html')



def userlogin(request):
    usr = request.POST['username']
    passw = request.POST['password']
    lobj = Login.objects.filter(username=usr, password=passw)

    if lobj.exists():
        lobjj = Login.objects.get(username=usr, password=passw)
        if lobjj.type == 'user':
            lid = lobjj.id
            return JsonResponse({'status': 'ok', 'lid': str(lid)})
        else:
            return JsonResponse({'status': 'no'})

    else:
        return JsonResponse({'status': 'no'})




def user_signup(request):
    name=request.POST['name']
    photo=request.POST['photo']
    phone=request.POST['phone']
    email=request.POST['email']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    gender=request.POST['gender']
    password=request.POST['password']
    confirmpass=request.POST['confirm']


    from datetime import datetime
    import base64
    date=datetime.now().strftime('%Y%m%d-%H%M%S%F')
    a=base64.b64decode(photo)
    fh=open("C:\\Users\\sidharth\\Documents\\GitHub\\Aicctv\\media\\user\\"+date+".jpg","wb")
    path='/media/user/'+date+".jpg"
    fh.write(a)
    fh.close()




    lg=Login()
    lg.username=email
    lg.password=confirmpass
    lg.type='user'
    lg.save()

    ug=User()
    ug.name=name
    ug.photo=path
    ug.phone=phone
    ug.email=email
    ug.place=place
    ug.post=post
    ug.pin=pin
    ug.district=district
    ug.gender=gender
    ug.LOGIN=lg
    ug.save()
    return JsonResponse({'status': 'ok'})




def and_viewprofile(request):
    lid=request.POST['lid']
    var=User.objects.get(LOGIN_id=lid)
    return  JsonResponse({'status':'ok',
                          'name':var.name,
                          'email':var.email,
                          'phone':var.phone,
                          'photo':var.photo,
                          'gender':var.gender,
                          'place':var.place,
                          "post":var.post,
                          'district':var.district,
                          'pin':var.pin,
                      })




def and_changepassword(request):
    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    lid=request.POST['lid']
    log = Login.objects.get(id=lid, password=currentpassword)
    if newpassword == confirmpassword:
        log1 = Login.objects.filter(id=lid).update(password=confirmpassword)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'ok'})


def user_edit_profile(request):
    name = request.POST['name']
    photo = request.POST['photo']
    phone = request.POST['phone']
    email = request.POST['email']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    gender = request.POST['gender']
    lid = request.POST['lid']
    ug = User.objects.get(LOGIN_id=lid)

    if len(photo)>1:


        from datetime import datetime
        import base64
        date = datetime.now().strftime('%Y%m%d%H%M%S%F')
        a = base64.b64decode(photo)
        fh = open("C:\\Users\\sidharth\\Documents\\GitHub\\Aicctv\\media\\user\\" + date + ".jpg", "wb")
        path = '/media/user/' + date + ".jpg"
        fh.write(a)
        fh.close()
        ug.photo = path
        ug.save()

    ug.name = name
    ug.phone = phone
    ug.email = email
    ug.place = place
    ug.post = post
    ug.pin = pin
    ug.district = district
    ug.gender = gender
    ug.save()
    return JsonResponse({'status': 'ok'})


def user_view_family_members(request):
    lid=request.POST['lid']
    res=family.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({
            'id':i.id,
            'name':i.name,
            'email':i.email_id,
            'phone':i.phone,
            'place':i.place,
            'relation':i.relation,
            'photo':i.photo,

        })
    return JsonResponse({'status': 'ok','data':l})


def user_add_family_members_post(request):
    lid=request.POST['lid']
    name = request.POST['name']
    photo = request.POST['photo']
    relation = request.POST['relation']
    place = request.POST['place']
    phone = request.POST['phone']
    email_id = request.POST['email']
    oo=family()
    oo.USER=User.objects.get(LOGIN_id=lid)
    from Aicctv import settings
    import base64
    a = base64.b64decode(photo)
    import datetime
    dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
    open(settings.MEDIA_ROOT+'\\family\\'+dt, 'wb').write(a)
    oo.photo = '/media/family/'+dt
    oo.name = name
    oo.phone = phone
    oo.email_id = email_id
    oo.place = place
    oo.relation = relation
    oo.place = place
    oo.save()
    return JsonResponse({'status': 'ok'})

def user_edit_profile_get(request):
    fid=request.POST['fid']
    res=family.objects.get(id=fid)
    return JsonResponse({'status': 'ok',
                         'name':res.name,
                         'photo':res.photo,
                         'relation':res.relation,
                         'place':res.place,
                         'email':res.email_id,
                         'phone':res.phone
                         })


def user_edit_family_members_post(request):
    fid=request.POST['fid']
    name = request.POST['name']
    photo = request.POST['photo']
    relation = request.POST['relation']
    place = request.POST['place']
    phone = request.POST['phone']
    email_id = request.POST['email_id']
    oo=family.objects.get(id=fid)
    if len(photo)> 5:
        from Aicctv import settings
        import base64
        a = base64.b64decode(photo)
        import datetime
        dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
        open(settings.MEDIA_ROOT+'\\family\\'+dt, 'wb').write(a)
        oo.photo = '/media/family/'+dt
        oo.save()

    oo.name = name
    oo.phone = phone
    oo.email_id = email_id
    oo.place = place
    oo.relation = relation
    oo.place = place
    oo.save()
    return JsonResponse({'status': 'ok'})



def delete_family_person(request):
    sid=request.POST['sid']
    res=family.objects.get(id=sid).delete()
    return JsonResponse({'status': 'ok'})



def send_complaints(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']
    res=Complaints()
    res.complaint=complaint
    res.reply='pending'
    res.status='pending'
    from datetime import datetime
    res.date=datetime.now().strftime('%Y-%m-%d')
    res.USER=User.objects.get(LOGIN_id=lid)
    res.save()
    return JsonResponse({'status': 'ok'})


def view_user_reply(request):
    lid=request.POST['lid']
    res=Complaints.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({
            'id': i.id,
            'date':i.date,
            'complaint': i.complaint,
            'reply': i.reply,
            'status': i.status,
        })


    return JsonResponse({'status': 'ok','data':l})




def send_review(request):
    lid=request.POST['lid']
    reviews=request.POST['review']
    rating=request.POST['rating']
    res=review()
    res.review=reviews
    res.rating=rating
    from datetime import datetime
    res.date=datetime.now().strftime('%Y-%m-%d')
    res.USER=User.objects.get(LOGIN_id=lid)
    res.save()
    return JsonResponse({'status': 'ok'})


def user_view_criminals(request):
    res=Criminals.objects.all()
    l=[]
    for i in res:
        l.append({
            'id':i.id,
            'name':i.name,
            'gender':i.gender,
            'place':i.place,
            'details':i.details,
            'photo':i.photo,

        })
    return JsonResponse({'status': 'ok','data':l})

def user_view_policestation(request):
    res = Police_Station.objects.all()
    l = []
    for i in res:
        l.append({
            'id': i.id,
            'LOGIN_id': i.LOGIN.id,
            'station_name': i.station_name,
            'SI_name': i.SI_name,
            'place': i.place,
            'post': i.post,
            'pin': i.pin,
            'district': i.district,
            'phone': i.phone,
            'email_id': i.email_id,

        })
    return JsonResponse({'status': 'ok', 'data': l})

def user_view_suspicious(request):
    res = SuspiciousActivities.objects.all()
    l = []
    for i in res:
        l.append({
            'id': i.id,
            'date': i.date,
            'time': i.time,
            'photo': i.photo,
            'activity': i.activity,
            'place': i.place,
            'name': i.CRIMINAL.name,

        })
    return JsonResponse({'status': 'ok', 'data': l})


def forward_suspicious_activity_post(request):
    dates=request.POST['date']
    time=request.POST['time']
    criminal=request.POST['cr']
    place=request.POST['place']
    activity=request.POST['activity']
    photo=request.FILES['photo']

    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    obj=SuspiciousActivities()
    obj.date=dates
    obj.time=time
    obj.activity=activity
    obj.CRIMINAL_id=criminal
    obj.photo=path
    obj.place=place
    obj.save()
    return JsonResponse({'status': 'ok'})

def view_detect_det(request):
    if request.session['lid'] != '':
        cobj = detection.objects.all()
        l=[]
        for i in cobj:
            if i.type=='criminal':
                name=Criminals.objects.get(id=i.did)
                l.append({"name":name.name,"station":name.POLICE.station_name,"date":i.date,"photo":i.photo,"time":i.time})
            if i.type=='unknown':
                name="un"
                l.append({"name":name,"station":name,"date":i.date,"photo":i.photo,"time":i.time})
                print(l)
        return render(request, 'ADMIN/view_detect_det.html', {"data": l})
    else:
        return HttpResponse('''<script>alert('Please login');window.location='/myapp/login/'</script>''')



def search_view_detect_det(request):
    if request.session['lid'] != '':
        frm = request.POST['fdate']
        to = request.POST['tdate']
        comp = detection.objects.filter(date__range=[frm, to])
        return render(request, 'ADMIN/view_detect_det.html', {"data": comp})
    else:
        return HttpResponse('''<script>alert('Please login');window.location='/myapp/login/'</script>''')
def p_view_detect_det(request):
    if request.session['lid'] != '':
        cobj = detection.objects.all()
        return render(request, 'POLICE/view_detect_det.html', {"data": cobj})
    else:
        return HttpResponse('''<script>alert('Please login');window.location='/myapp/login/'</script>''')

def p_search_view_detect_det(request):
    if request.session['lid'] != '':
        frm = request.POST['fdate']
        to = request.POST['tdate']
        comp = detection.objects.filter(date__range=[frm, to])
        return render(request, 'POLICE/view_detect_det.html', {"data": comp})
    else:
        return HttpResponse('''<script>alert('Please login');window.location='/myapp/login/'</script>''')
def View_Detected_Criminal(request):
    robj=detection.objects.all()
    l=[]
    for i in robj:
        l.append({'id':i.id,'cname':i.CRIMINAL.name,'photo':i.CRIMINAL.photo,'date':i.date,'time':i.time})
    print(l)
    return JsonResponse({'status': "ok",'data':l})
def View_Detected_Criminal_search(request):
    search=request.POST['search']
    robj=detection.objects.filter(date__contains=search)
    l=[]
    for i in robj:
        l.append({'id':i.id,'cname':i.CRIMINAL.name,'photo':i.CRIMINAL.photo,'date':i.date,'time':i.time})
    print(l)
    return JsonResponse({'status': "ok",'data':l})
