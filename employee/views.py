from django.shortcuts import render
import requests

# Create your views here.
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    r = requests.post('http://ec2-13-233-193-38.ap-south-1.compute.amazonaws.com/login',data={'username':'admin','password':'admin@123'})
    p = r.json()['access_token']
    tr=requests.get('http://ec2-13-233-193-38.ap-south-1.compute.amazonaws.com/drivers',headers={'Authorization':f'Bearer {p}'})
    drivers=tr.json()
    return render(request,"show.html",{'employees':drivers})
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")
