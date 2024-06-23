from rest_framework.views import APIView
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework import status

from .models import Staffs
from .serializers import StaffSerializer


# Create your views here.

class StaffView(APIView):
    
    def get_staff(self,id):
        try:
            staff = Staffs.objects.get(staff_id = id)
            return staff
        except Staffs.DoesNotExist:
            raise Http404
        
    def get(self, request, id = None):
        if id:
            data = self.get_staff(id)
            serializer = StaffSerializer(data)
            return Response(serializer.data)
        else:
            data = Staffs.objects.all()
            serializer = StaffSerializer(data, many = True)
            return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        serializer = StaffSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Staff Created Successffully", safe = False)
        return JsonResponse("Failed to add Staff data", safe=False)
    
    def put(self, request, id):
        staff_update = Staffs.objects.get(staff_id = id)
        serializer = StaffSerializer(staff_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Staff Updated Successfully", safe=False, status=status.HTTP_200_OK)
        return JsonResponse("Failed to add Student Data", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            staff_delete = Staffs.objects.get(staff_id = id)
            staff_delete.delete()
            return JsonResponse("Staff Deleted Successfully", safe=False, status=status.HTTP_204_NO_CONTENT)
        except Staffs.DoesNotExist:
            return JsonResponse("Staff does not exist", safe=False, status=status.HTTP_404_NOT_FOUND)
            
        