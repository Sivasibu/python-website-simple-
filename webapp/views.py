from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from. models import Students
from. serializers import StudentSerializer
from rest_framework .permissions import IsAuthenticated
from rest_framework import filters
from rest_framework .renderers import JSONRenderer,TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
# Create your views here.

class webappView(APIView):
    renderer_classes =(JSONRenderer,TemplateHTMLRenderer)
    template_name ="Home.html"
    
    
    def get(self, request):
        queryset = Students.objects.all()
        return Response({'data': queryset})
       

class StudentView(ModelViewSet):

    serializer_class = StudentSerializer
    permission_classes =[IsAuthenticated]
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    
    ordering_fields =['id','first_name','roll_number','address']
    search_fields =['first_name','last_name','address','roll_number','mobile']

    def get_queryset(self):
        return Students.objects.filter()


       

def deleteData(request,id):
    mydata =Students.objects.get(id=id)
    mydata.delete()
    return redirect('basic')

