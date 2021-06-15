from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import taskeform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from  django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class tasklist(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 'tas'

class taskdetail(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'tas'

class taskupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','prio','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk': self.object.id})


class taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlist')











def index(request):
    tas = task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name','')
        prio = request.POST.get('prio','')
        date = request.POST.get('date', '')

        tasks=task(name=name, prio=prio,date=date)
        tasks.save()
    return render(request,'index.html',{'task':tas})



def delete(request,id):
    if request.method=='POST':
        tas=task.objects.get(id=id)
        tas.delete()
        return redirect('/')
    return render(request,'delete.html')



def update(request,id):
    tas=task.objects.get(id=id)
    form=taskeform(request.POST or None, request.FILES,instance=tas)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html', {'form':form,'tas':tas})

#
# def details(request):
#     tas=task.objects.all()
#     return  render(request,"details.html",{'task':tas})