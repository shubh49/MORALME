from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms.models import signup
from forms.models import signupform
import pdb

# Create your views here.
def getdetails(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            f=form.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = signupform()
        return render(request,'forms/forms.html',{'form': form})
    
def thanks(request):
   return render(request,'forms/thanks.html')

