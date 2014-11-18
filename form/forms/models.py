from django.db import models
# Create your models here.
from django import forms
from django.forms import ModelForm

class signup(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=15)
    email = models.EmailField()
    pwd = models.CharField(max_length=15)
    
    def __unicode__(self):
        return "{0} {1} {2} {3} {4}".format(
            self,self.name,self.uname,self.email,self.pwd)
    
class signupform(ModelForm):
    class Meta:
        model = signup
        fields = ['name','uname','email','pwd']
 
    
    
    

    


