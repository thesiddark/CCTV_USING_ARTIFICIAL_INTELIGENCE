from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *

def admin_home(request):
    return render(request,'ADMIN/admin homepage.html')


def login(request):
    return render(request,'LOGIN.html')

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
            return HttpResponse('''<script>alert("Welcome Police Home");window.location='/myapp/homepage/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid");window.location='/myapp/login/'</script>''')


def admin_add_police(request):
    return render(request,'ADMIN/admin add police.html')

def admin_add_police_post(request):
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
   return render(request,'ADMIN/admin change password.html')

def admin_change_password_post(request):
    currentpassword = request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']

    abc=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if abc.exists():
        if newpassword==confirmpassword:
            abc = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("success");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/myapp/admin_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid");window.location='/myapp/admin_change_password/'</script>''')



def admin_complaints(request):
    var = Complaints.objects.all()
    return render(request,'ADMIN/admin complaints.html',{'data':var})

def admin_complaints_post(request):
    fromdate=request.POST['from']
    todate = request.POST['to']
    return render(request, 'ADMIN/admin complaints.html')

def admin_edit_police(request,id):
    res=Police_Station.objects.get(id=id)
    return render(request,'ADMIN/admin edit police.html',{'data':res})

def admin_edit_police_post(request):
    stationname=request.POST['station']
    siname = request.POST['siname']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phone= request.POST['phone']
    district = request.POST['district']
    emailid = request.POST['emailid']
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
    return HttpResponse('''<script>alert("edited");window.location='/myapp/view_police/'</script>''')

def admin_suspicious_activity(request):
    var = SuspiciousActivities.objects.all()
    return render(request,'ADMIN/admin suspicious activity.html',{'data':var})

def admin_suspicious_activity_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    return render(request, 'ADMIN/admin suspicious activity.html')

def admin_view_appreviews(request):
    var = review.objects.all()
    return render(request,'ADMIN/admin view AppReviews.html',{'data':var})

def admin_view_appreviews_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    return render(request, 'ADMIN/admin view AppReviews.html')

def admin_view_criminals(request):
    var = Criminals.objects.all()
    return render(request,'ADMIN/admin view criminals.html',{'data':var})

def admin_view_criminals_post(request):
    search=request.POST['textfield']
    var = Criminals.objects.filter(name__icontains=search)
    return render(request, 'ADMIN/admin view criminals.html',{'data':var})

def admin_view_police(request):
    var=Police_Station.objects.all()
    return render(request,'ADMIN/admin view police.html',{'data':var})

def admin_view_police_post(request):
    search = request.POST['name']
    var = Police_Station.objects.filter(station_name__icontains=search)
    return render(request, 'ADMIN/admin view police.html', {'data': var})
def admin_delete_police(request,id):
    data=Police_Station.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/myapp/view_police/"</script>''')


def admin_view_registered_users(request):
    var = User.objects.all()
    return render(request,'ADMIN/admin view registered users.html',{'data':var})

def admin_view_registered_users_post(request):
    search = request.POST['name']
    var = User.objects.filter(name__icontains=search)
    return render(request, 'ADMIN/admin view registered users.html',{'data': var})

#users

def user_add_family_members(request):
   return render(request,'user/user add family members.html')

def user_add_family_members_post(request):
    name = request.POST['name']
    photo = request.POST['photo']
    relation = request.POST['relation']
    place = request.POST['place']
    phone = request.POST['phone']
    emailid = request.POST['email_id']
    return HttpResponse("ok")

def user_chat(request):
   return render(request,'user/user chat.html')

def user_chat_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    message = request.POST['message']
    return HttpResponse("ok")

def user_review(request):
    
   return render(request,'user/user review.html')
def user_review_post(request):
    review = request.POST['review']
    return HttpResponse("ok")

def user_view_and_edit_profile(request):
   return render(request,'user/user view and edit profile.html')

def user_view_and_edit_profile_post(request):
    name = request.POST['name']
    emailid = request.POST['email id']
    phone = request.POST['phone']
    place = request.POST['PLACE']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    gender = request.POST['gender']
    return HttpResponse("ok")

def user_view_criminals(request):
   return render(request,'user/user view criminals.html')

def user_view_criminals_post(request):
    name = request.POST['name']
    return render(request,'user/user view criminals.html')

def user_view_family_members(request):
   return render(request,'user/user view family member.html')

def user_view_family_members_post(request):
    name = request.POST['name']
    return render(request,'user/user view family member.html')

#police

def police_add_criminals(request):
   return render(request,'police/police add criminals.html')

def police_add_criminals_post(request):
    name = request.POST['name']
    photo = request.POST['photo']
    details = request.POST['details']
    return HttpResponse("ok")

def police_view_criminals(request):
   return render(request,'police/police view criminals.html')

def police_view_criminals_post(request):
    name = request.POST['name']
    return render(request,'police/police view criminals.html')