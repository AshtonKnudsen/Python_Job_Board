from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, User


def LoadPage(request):
    if not "id" in request.session:
        return redirect("/")
    context = {
        "jobs" : Job.objects.all().order_by("-created_at"),
    }
    return render(request,'Display/Page.html', context)

def view(request,id):
    if not "id" in request.session:
        return redirect("/")
    context = {
        "job" : Job.objects.get(id=id)
    }
    return render(request, 'Display/viewJob.html',context)

def new(request):
    if not "id" in request.session:
        return redirect("/")
    return render(request, 'Display/newJob.html')

def process_new(request):
    errors = Job.objects.Job_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/Display/new")
    id = request.session["id"]
    if request.method == "POST":
        x = User.objects.get(id=id)
        Job.objects.create(user=x, job_title=request.POST["title"], location=request.POST["location"],description=request.POST["description"])
    return redirect("/Display/LoadPage")

def delete(request, id):
    if not request.session["id"] == x.user.id:
        return redirect("https://www.youtube.com/watch?v=XdKryknE2G8")
    comment_to_delete = Job.objects.get(id=id)
    comment_to_delete.delete()
    return redirect("/Display/LoadPage")

def edit(request,id):
    context={
        "id" : id
    }
    return render(request, "Display/editJob.html",context)

def process_edit(request, id):
    if not "id" in request.session:
        return redirect("/")
    x = Job.objects.get(id=id)
    if not request.session["id"] == x.user.id:
        return redirect("https://www.youtube.com/watch?v=XdKryknE2G8")
    errors = Job.objects.Job_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/Display/edit/{id}")
    if request.method == "POST":
        job_to_update = x
        job_to_update.job_title = request.POST["title"]
        job_to_update.location = request.POST["location"]
        job_to_update.description = request.POST["description"]
        job_to_update.save()
        return redirect("/Display/LoadPage")

