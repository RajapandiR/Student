from django.db import models
from myproject import settings

# Create your models here.

class StudentModel(models.Model):

    stud_id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=200)
    RollNo = models.CharField(max_length = 200, unique = True)
    DOB = models.DateField(null= True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Name

class StudentMarkModel(models.Model):
    stud_id = models.ForeignKey(StudentModel, on_delete = models.CASCADE, null = True)
    mark = models.IntegerField()

    # def __str__(self):
    #     return self.stud_id