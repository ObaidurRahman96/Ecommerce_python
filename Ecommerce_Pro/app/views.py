from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm

def IndexView(request):
    app= Project.objects.all()
    context= {'projects' :app}
    return render(request , 'index.html', context)

def ProjectView(request, pk):
    projectObj=Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {'project' : projectObj,})

#Post data into database
def createProject(request):
    form=ProjectForm()

    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('IndexView')
    contex={'form' : form}
    return render(request, 'projects/project_form.html', contex)

#update data via browser
def updateProject(request, pk):
    app=Project.objects.get(id=pk)
    form=ProjectForm(instance=app)

    if request.method=='POST':
        form=ProjectForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('IndexView')
    contex={'form' : form}
    return render(request, 'projects/project_form.html', contex)
