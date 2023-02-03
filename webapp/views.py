from django.shortcuts import render,redirect,HttpResponse
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
from django.template import loader
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





# def updateData(request,id):
#       student = Students.objects.get(id=id)
#       template =loader.get_template("update.html")
#       context ={"student":student}
#       return HttpResponse(template.render(context,request))



def addData(request):
   if request.method=='POST':
      first_name =request.POST['first_name']
      last_name =request.POST['last_name']
      address =request.POST['address']
      roll_number =request.POST['roll_number']
      mobile =request.POST['mobile']
      obj=Students(first_name=first_name,last_name=last_name,address=address,roll_number=roll_number,mobile=mobile)
      obj.save()
      queryset=Students.objects.all()
      return render(request,'Home.html',{'data':queryset})
      return redirect('Home')
   return render(request,'Home.html')   

def updaterecord(request,id):
    queryset =Students.objects.get(id=id)
    print(queryset)
    if request.method=='POST':
      first_name =request.POST['first_name']
      last_name =request.POST['last_name']
      address =request.POST['address']
      roll_number =request.POST['roll_number']
      mobile =request.POST['mobile']
      queryset.first_name=first_name
      queryset.last_name=last_name
      queryset.address=address
      queryset.roll_number=roll_number    
      queryset.mobile=mobile
      queryset.save()
      return redirect('Home')
    return render(request,'update.html',{'students':queryset})


def deleteData(request,id):
      queryset =Students.objects.get(id=id)
      queryset.delete()
      return redirect('Home')