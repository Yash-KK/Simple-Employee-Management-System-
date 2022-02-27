# from ast import Add
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Employee,Department,Role
from django.db.models import Q
from .forms import AddEmp


# Create your views here.
def index(request):
    return render(request,"App1/index.html")

def view_all(request):
    emp = Employee.objects.all()
    return render(request,"App1/viewall.html",{
        "emp":emp
    })

def add_emp(request):
    if request.method == "POST":
        form = AddEmp(request.POST)
        if form.is_valid():
            Employee.objects.create(first_name=form.cleaned_data["f_name"],
            last_name=form.cleaned_data["l_name"],
            dept_id=form.cleaned_data["dept"],
            salary=form.cleaned_data["salary"],
            bonus=form.cleaned_data["bonus"],
            role_id=form.cleaned_data["role"],
            phone=form.cleaned_data["phone"])            
            return HttpResponse("Thank You!")

    else:        
        form = AddEmp()
    return render(request,"App1/add.html",{
        "form":form
    })

def remove_emp(request):
    emps = Employee.objects.all()
    return render(request,"App1/remove.html",{
        "emps":emps
    })
def remove(request,id):
        try:
            data = Employee.objects.get(id=id)
            data.delete()
            return HttpResponse("Removed")
        except:
            return Http404("Error! Invalid ID")    
        
def filte_emp(request):
    if request.method == "POST":
        name = request.POST['flname']
        dept = request.POST['department']
        role = request.POST['role']
        data = Employee.objects.all()
        if name:
            emp = data.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emp = data.filter(dept__name__contains=dept)
        if role:
            emp = data.filter(role__name__contains=role)

        return render(request,"App1/viewall.html",{
            "emp":emp
        })            
    return render(request,"App1/filter.html",{
        
    })
