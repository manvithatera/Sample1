from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Employee
from .forms import EmployeeForm, RawEMployeeForm

# Create your views here.


def detail_lookup_view(request,my_id):

    try:
        obj = Employee.objects.get(id=my_id)
    except Employee.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, "employee/emp_detail.html", context)

def employee_create_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EmployeeForm()
    context = {
        'form' : form
    }
    return render(request, "employee/emp_create.html", context)

def employee_detail_view(request):
    obj = Employee.objects.get(id = 1)

    context = {
        'object' : obj
    }
    return render(request, "employee/emp_detail.html", context)

def employee_list_view(request):
    queryset = Employee.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "employee/emp_list.html", context)

def employee_delete_view(request,my_id):
    obj = Employee.objects.get(id = my_id)
    if request.method == "POST":
        obj.delete()
    context = {
        'object' : obj
    }
    return render(request, "employee/emp_delete.html", context)