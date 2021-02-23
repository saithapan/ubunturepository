from django.contrib import admin
from .models import task_list,user_profile,customer_profile,task_list2,student_test,mark_test,test_form
# Register your models here.

admin.site.register(task_list)
admin.site.register(user_profile)
admin.site.register(customer_profile)
admin.site.register(task_list2)
admin.site.register(student_test)
admin.site.register(mark_test)
admin.site.register(test_form)