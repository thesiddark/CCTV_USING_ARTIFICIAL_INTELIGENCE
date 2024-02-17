from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class Police_Station(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=100)
    SI_name= models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    post= models.CharField(max_length=100)
    email_id= models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    phone= models.BigIntegerField()
    pin= models.BigIntegerField()


class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    district=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)


class Complaints(models.Model):
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateField()
    complaint= models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    reply= models.CharField(max_length=100)



class Criminals(models.Model):
    photo = models.CharField(max_length=500)
    photo1 = models.CharField(max_length=500)
    photo2 = models.CharField(max_length=500)
    details= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    post= models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    pin= models.BigIntegerField()
    POLICE= models.ForeignKey(Police_Station,on_delete=models.CASCADE)



class SuspiciousActivities(models.Model):
    date= models.DateField()
    place= models.CharField(max_length=100)
    time= models.CharField(max_length=100)
    photo= models.CharField(max_length=500)
    CRIMINAL= models.ForeignKey(Criminals,on_delete=models.CASCADE)
    activity= models.CharField(max_length=100)

class review(models.Model):
    date= models.DateField()
    review= models.CharField(max_length=100)
    USER= models.ForeignKey(User,on_delete=models.CASCADE)
    rating= models.CharField(max_length=100)

class Chat(models.Model):
    date = models.DateField()
    message=models.CharField(max_length=100)
    FROMID=models.ForeignKey(Login, on_delete=models.CASCADE,related_name="fuser")
    TOID=models.ForeignKey(Login, on_delete=models.CASCADE,related_name="tuser")

class family(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    relation= models.CharField(max_length=100)
    photo= models.CharField(max_length=500)
    place= models.CharField(max_length=100)
    email_id= models.CharField(max_length=100)
    phone= models.BigIntegerField()


#
#
# class detect(models.Model):
#     date=models.DateField()
#     time=models.CharField(max_length=100)
#     image= models.CharField(max_length=500)
#
#
#
#
# class detect_sub(models.Model):
#     CRIMINAL = models.ForeignKey(Criminals, on_delete=models.CASCADE)
#     DETECT = models.ForeignKey(detect, on_delete=models.CASCADE)


class detection(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=100)
    CRIMINAL = models.ForeignKey(Criminals, on_delete=models.CASCADE)

