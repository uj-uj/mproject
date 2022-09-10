from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import GeeksForm
from .models import Geek  
from django.http import HttpResponseRedirect

def index(request):
    g=Geek.objects.all()[1]
    if request.method == 'POST':
        form = GeeksForm(request.POST,instance=g)
        if form.is_valid():
            form.save()
            print("done ",form)
            return HttpResponse("done")
    form=GeeksForm(instance=g)
    context={'context':form}
    return render(request,'formcheck/home.html',context)