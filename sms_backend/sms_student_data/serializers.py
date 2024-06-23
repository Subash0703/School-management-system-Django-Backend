from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('student_id',
                  'StudentName',
                  'RegisterNumber',
                  'RollNumber',
                  'Course',
                  'Batch')