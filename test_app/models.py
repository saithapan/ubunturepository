from django.db import models

# Create your models here.

class task_list(models.Model):
    title = models.CharField(max_length= 111)
    name = models.CharField(max_length = 111)
    description  = models.TextField()
    number = models.BooleanField()

    def __str__(self):
        return self.title


class user_profile(models.Model):
    fname = models.CharField(max_length= 100)
    lname = models.CharField(max_length= 100)
    technology = models.CharField(max_length = 100)
    email = models.EmailField(default = None)
    display_picture = models.FileField()

    def __str__(self):
        return self.fname



class customer_profile(models.Model):
    c_name = models.CharField(max_length = 200)
    c_address = models.TextField()
    c_file = models.FileField()
    c_email = models.EmailField(default=None)

    def __str__(self):
        return self.c_name


class task_list2(models.Model):
    task_name = models.CharField(max_length = 100)
    task_title = models.CharField(max_length = 100)
    task_email = models.EmailField(default = None)
    task_number = models.BooleanField()

    def __str__(self):
        return self.task_name


class student_test(models.Model):
    stid = models.IntegerField(primary_key=True)
    stdname = models.CharField(max_length=100)

    def __str__(self):
        return self.stdname

class mark_test(models.Model):
    marks_id = models.IntegerField(primary_key = True)
    social = models.CharField(max_length=100)
    science = models.CharField(max_length = 100)
    maths = models.CharField(max_length = 100)
    stid = models.ForeignKey(student_test,related_name='marks',on_delete= models.CASCADE)

    def __str__(self):
        return self.social

class test_form(models.Model):
    test_name = models.CharField(max_length=100)
    test_region = models.CharField(max_length=100)
    test_country = models.CharField(max_length=100)
    test_village = models.CharField(max_length=100)

    def __str__(self):
        return self.test_name