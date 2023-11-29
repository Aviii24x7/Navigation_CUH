from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50)
    Dean = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    school_description = models.TextField(max_length=300)
    slugy = models.SlugField(unique=True, db_index = True)

    def __str__(self):
        return self.school_name
    

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    head_name = models.CharField(max_length=70)
    dept_description = models.TextField(null=True,max_length=300)
    
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, related_name="departments")
    
    slug = models.SlugField(unique=True, db_index=True)
    
    def __str__(self) -> str:
        return f"{self.dept_name}"

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    office = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name="teachers", on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to="teacher", null=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    