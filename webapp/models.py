from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
  
    first_name =models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=20)
    updated_by =models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="updated_by")

    def __str__(self):
        
        return self.first_name+ " "+self.last_name

