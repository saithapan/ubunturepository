from rest_framework import serializers

from .models import StudentModel,MarksModel

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarksModel
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    marks = MarksSerializer(read_only = True, many=True)
    class Meta:
        model = StudentModel
        fields = '__all__'
