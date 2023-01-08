from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo_app.models import Task
from . forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy



class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tsk'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_view = 'tsk'
    fields = ('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')





def add(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        task = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date')
        obj = Task(task=task,priority=priority,date=date)
        obj.save()
    return render(request,'home.html',{"tsk":task1})

def delete(request,taskid):
    t = Task.objects.get(id=taskid)
    if request.method == "POST":
        t.delete()
        return redirect('/')
    return render(request,'delete.html',{"obj1":t})

def update(request,id):
    task = Task.objects.get(id=id)
    form = Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'tsk1':task,'form':form})



