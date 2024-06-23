from django.db import models

# Create your models here.

class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    RegisterNumber = models.IntegerField()
    RollNumber = models.IntegerField()
    Course = models.CharField(max_length=100)
    Batch = models.CharField(max_length=100)

    def __str__(self):
        return self.StudentName
