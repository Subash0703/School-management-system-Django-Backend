from django.db import models
import uuid

# Create your models here.

class Staffs(models.Model):
    staff_id = models.AutoField(primary_key=True)
    StaffName = models.CharField(max_length=100)
    StaffMail = models.EmailField()
    StaffNumber = models.IntegerField()
    staffReg_id = models.UUIDField(default=uuid.uuid4)
    staffCourse = models.CharField(max_length=100)
    
    def __str__(self):
        return self.StaffName