from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Department, Teacher
from django.views import View


# Create your views here.
def home(request):
    return render(request, 'navapp/home.html')

class AllDeptView(ListView):
    template_name="navapp/all_dept.html"
    model = Department
    context_object_name = "all_dept"

# class AllTeacherView(ListView):
#     template_name="navapp/dept_teachers.html"
#     model = Teacher
#     context_object_name = "all_teachers"

class SingleDeptView(View):
    
    def get(self,request,slug):
        dept = Department.objects.get(slug=slug)
        
        context={
            "dept": dept,
            "all_teachers" : dept.teachers.all().order_by("id")
            
        }
        return render(request,"navapp/dept_teachers.html",context)
    
        