from django.db import models
class Usersdata(models.Model):
    firstname=models.CharField(max_length=100,default=False)
    lastname=models.CharField(max_length=100,unique=True)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    timezone=models.CharField(max_length=100,blank=True,null=True)
    language=models.CharField(max_length=100,blank=True,null=True)
class qr(models.Model):
    eventid=models.CharField(max_length=30,default=False,unique=True)
    
# Create your models here.
class Teamreg(models.Model):
    fullname=models.CharField(max_length=20,unique=True)
    squadname=models.CharField(max_length=20,unique=True,default=True)
    squadlogo=models.CharField(max_length=30, null=True)
    team1name=models.CharField(max_length=30)
    team2name=models.CharField(max_length=30)
    team3name=models.CharField(max_length=30,default=False)
    team4name=models.CharField(max_length=30,default=False)
    team5name=models.CharField(max_length=30,default=False)
    team6name=models.CharField(max_length=30,default=False)
    team1id=models.CharField(max_length=30,default=False)
    team2id=models.CharField(max_length=30,default=False)
    team3id=models.CharField(max_length=30,default=False)
    team4id=models.CharField(max_length=30,default=False)
    team5id=models.CharField(max_length=30,default=False)
    team6id=models.CharField(max_length=30,default=False)
    emailid=models.CharField(max_length=10,default=False)

    phone=models.CharField(max_length=12,default=False)
    notifphone=models.CharField(max_length=12,default=False)
class BookedHistory(models.Model):
    username=models.CharField(max_length=20,default=False)
    amount=models.CharField(max_length=20)
    eventid=models.CharField(max_length=30,default=False)
    date=models.CharField(max_length=10)
