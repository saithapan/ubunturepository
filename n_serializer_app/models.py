from django.db import models

# Create your models here.
class StudentModel(models.Model):
    stid = models.IntegerField(primary_key = True)
    stname = models.CharField(max_length=100)

class MarksModel(models.Model):
    Marksid = models.IntegerField(primary_key = True)
    maths = models.IntegerField()
    physics = models.IntegerField()
    computers = models.IntegerField()
    stid = models.ForeignKey(StudentModel,related_name = 'marks', on_delete = models.CASCADE)