from django.db import models
class Users(models.Model):
    email = models.CharField(max_length=60,default=True,unique=True)
    firstname=models.CharField(max_length=60,default=False)
    lastname=models.CharField(max_length=60,default=False)
    password=models.CharField(max_length=60,default=False)
    timezone=models.CharField(max_length=60,default=False)
    language=models.CharField(max_length=60,default=False)
    
