from rest_framework import serializers
from .models import task_list,task_list2,mark_test,student_test

class task_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_list
        # fields = ('title','name','description')
        fields = '__all__'


class task_list_newSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_list2
        fields = '__all__'

class mark_testSerializer(serializers.ModelSerializer):
    class Meta:
        model = mark_test
        fields = '__all__'

class student_testSerializer(serializers.ModelSerializer):
    marks = mark_testSerializer(read_only = True, many=True)
    class Meta:
        model = student_test
        fields = '__all__'