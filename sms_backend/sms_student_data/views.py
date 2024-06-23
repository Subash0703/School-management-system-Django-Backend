from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework import status

from .models import Students
from .serializers import StudentSerializer

# Create your views here.

class StudentView(APIView):
    
    def get_student(self,id):
        try:
            student = Students.objects.get(student_id=id)
            return student
        except Students.DoesNotExist:
            raise Http404
        
    def get(self, request, id=None):
        if id:
            data = self.get_student(id)
            serializer = StudentSerializer(data)
        else:
            data = Students.objects.all()
            serializer = StudentSerializer(data, many = True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully", safe=False)
        return JsonResponse("Failed to add Student data", safe=False)
    
    def put(self, request, id):
        student_update = Students.objects.get(student_id=id)
        serializer = StudentSerializer(student_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Updated Successfully", safe=False, status=status.HTTP_200_OK)
        return JsonResponse("Failed to add Student data", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id): 
        try:
           student_delete = Students.objects.get(student_id=id)
           student_delete.delete()
           return JsonResponse("Student Deleted Successfully", safe=False, status=status.HTTP_204_NO_CONTENT)
        except Students.DoesNotExist:
           return JsonResponse("Student does not exist", safe=False, status=status.HTTP_404_NOT_FOUND)
    