from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    head_name = models.CharField(max_length=70)
    description = models.TextField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True)
    
    def __str__(self) -> str:
        return f"{self.dept_name}"

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    office = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name="teachers", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    