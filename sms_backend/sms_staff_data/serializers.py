from rest_framework import serializers
from .models import Staffs

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = ('staff_id',
                  'StaffName',
                  'StaffMail',
                  'StaffNumber',
                  'staffReg_id',
                  'staffCourse')