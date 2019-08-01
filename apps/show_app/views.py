from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# def update(request, id):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Shows.objects.basic_validator(request.POST)
#         # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#             # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#             # redirect the user back to the form to fix the errors  
#         return redirect('//edit/'+id)
#     else:
#             # if the errors object is empty, that means there were no errors!
#             # retrieve the blog to be updated, make the changes, and save
#         show = Shows.objects.get(id = id)
#         show.name = request.POST['name']
#         show.description = request.POST['description']
#         show.save()
#         messages.success(request, "Show successfully updated")
#             # redirect to a success route
#         return redirect('/shows')

def root(request):
    return redirect("show_app/shows")

def index(request):
    context = {
        "shows": Shows.objects.all()
    }
    return render(request, "show_app/show.html", context)

def add_show(request):
    return render(request, "show_app/add_new.html")

def create_show(request):
    errors = Shows.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0: 
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            
            # redirect the user back to the form to fix the errors  
            return redirect('/add_show')
    else:
        show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], description=request.POST['description'], release_date=request.POST['release_date'])

        id=str(show.id)
        return redirect("/show_info/"+id)

def show_info(request, num):
    context = {
        "shows": Shows.objects.get(id=num)
    }
    return render(request,"show_app/created_show.html", context)

def update_show(request, num):
    errors = Shows.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0: 
        x = Shows.objects.get(id=num)
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

            # redirect the user back to the form to fix the errors  
            return redirect('/edit_show/'+str(x.id))
    else:
        x = Shows.objects.get(id=num)
        x.title = request.POST['title']
        x.network = request.POST['network']
        x.realease_date = request.POST['release_date']
        x.description= request.POST['description']
        x.save()
        messages.success(request, "Show successfully updated")

        return redirect("/show_info/" + str(x.id))

def edit_show(request, num):
    context = {
        "shows": Shows.objects.get(id=num)
    }
    return render(request, "show_app/edit.html", context)

def destroy(request, num):
    show_to_delete = Shows.objects.get(id=num)	
    show_to_delete.delete()
    return redirect("/shows")
