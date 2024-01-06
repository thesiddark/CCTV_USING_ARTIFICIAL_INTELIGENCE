from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *


def login(request):
    return render(request,'LOGIN.html')

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    abc=Login.objects.filter( username=username,password=password)
    if abc.exists():
        abcd = Login.objects.filter(username=username, password=password)
        request.session["lid"]=abcd.id
        if abcd.type == 'admin':
            return HttpResponse('''<script>alert("Welcome Admin Home");window.location='/myapp/'</script>''')
        elif abcd.type == 'police':
            return HttpResponse('''<script>alert("Welcome Police Home");window.location='/myapp/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid");window.location='/myapp/login/'</script>''')


def admin_add_police(request):
    return render(request,'ADMIN/admin add police.html')

def admin_add_police_post(request):
    stationname=request.POST['station name']
    siname=request.POST['si name']
    place=request.POST['PLACE']
    post=request.POST['post']
    pin=request.POST['pin']
    emailid=request.POST['email id']
    phone=request.POST['phone']
    district= request.POST['district']
    return HttpResponse("ok")

def admin_change_password(request):
   return render(request,'ADMIN/admin change password.html')

def admin_change_password_POST(request):
    currentpassword = request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    return HttpResponse("ok")


def admin_complaints(request):
   return render(request,'ADMIN/admin complaints.html')

def admin_complaints_post(request):
    fromdate=request.POST['from']
    todate = request.POST['to']
    return render(request, 'ADMIN/admin complaints.html')

def admin_edit_police(request):
   return render(request,'ADMIN/admin edit police.html')

def admin_edit_police_post(request):
    stationname=request.POST['station']
    siname = request.POST['siname']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    emailid = request.POST['email id']
    return HttpResponse("ok")

def admin_suspicious_activity(request):
   return render(request,'ADMIN/admin suspicious activity.html')

def admin_suspicious_activity_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    return render(request, 'ADMIN/admin suspicious activity.html')

def admin_view_appreviews(request):
   return render(request,'ADMIN/admin view AppReviews.html')

def admin_view_appreviews_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    return render(request, 'ADMIN/admin view AppReviews.html')

def admin_view_criminals(request):
   return render(request,'ADMIN/admin view criminals.html')

def admin_view_criminals_post(request):
    name=request.POST['textfield']
    return render(request, 'ADMIN/admin view criminals.html')

def admin_view_police(request):
   return render(request,'ADMIN/admin view police.html')

def admin_view_police_post(request):
    search = request.POST['name']
    return render(request, 'ADMIN/admin view police.html')

def admin_view_registered_users(request):
   return render(request,'ADMIN/admin view registered users.html')

def admin_view_registered_users_post(request):
    search = request.POST['name']
    return render(request, 'ADMIN/admin view registered users.html')

#users

def user_add_family_members(request):
   return render(request,'user/user add family members.html')

def user_add_family_members_post(request):
    name = request.POST['name']
    photo = request.POST['photo']
    relation = request.POST['relation']
    place = request.POST['place']
    phone = request.POST['phone']
    emailid = request.POST['emailid']
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