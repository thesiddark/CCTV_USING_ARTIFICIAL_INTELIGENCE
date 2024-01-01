from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'LOGIN.html')

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    return HttpResponse("ok")

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
    fromdate=request.POST['textfield']
    todate = request.POST['textfield2']
    return render(request, 'ADMIN/admin complaints.html')

def admin_edit_police(request):
   return render(request,'ADMIN/admin edit police.html')

def admin_edit_police_post(request):
    stationname=request.POST['textfield']
    siname = request.POST['siname']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    emailid = request.POST['emailid']
    return HttpResponse("ok")

def admin_suspicious_activity(request):
   return render(request,'ADMIN/admin suspicious activity.html')

def admin_suspicious_activity_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    return render(request, 'ADMIN/admin suspicious activity.html')

def admin_view_appreviews(request):
   return render(request,'ADMIN/admin view AppReviews.html')

def admin_view_appreviews_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    return render(request, 'ADMIN/admin view AppReviews.html')

def admin_view_criminals(request):
   return render(request,'ADMIN/admin view criminals.html')

def admin_view_criminals_post(request):
    name=request.POST['textfield']
    return render(request, 'ADMIN/admin view criminals.html')

def admin_view_police(request):
   return render(request,'ADMIN/admin view police.html')

def admin_view_police_post(request):
    search = request.POST['textfield']
    return render(request, 'ADMIN/admin view police.html')

def admin_view_registered_users(request):
   return render(request,'ADMIN/admin view registered users.html')

def admin_view_registered_users_post(request):
    search = request.POST['textfield']
    return render(request, 'ADMIN/admin view registered users.html')
    