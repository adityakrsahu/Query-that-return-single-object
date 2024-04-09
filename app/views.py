from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.

def home(request):
    # get(coloumn_name=value)
    # user = Student.objects.get(id=2) # get arguments always used primary-key coloumn
    # user = Student.objects.get(stu_name="aditya Kumar")
    # user = Student.objects.get(stu_name="Arvind singh")
    # print(user.id, user.stu_name,user.stu_city)
    # return HttpResponse(user)
    
    ## first()
    # user = Student.objects.first()
    # # user = Student.objects.order_by('stu_name').first()
    # # user = Student.objects.order_by('-stu_name').first()
    # print(user.id, user.stu_name,user.stu_city)
    # return HttpResponse(user)

    # last()
    # user = Student.objects.last()
    # # user = Student.objects.order_by('stu_name').last()
    # # user = Student.objects.order_by('-stu_name').last()
    # print(user.id, user.stu_name,user.stu_city)
    # return HttpResponse(user)

    # # latest(*fields/Coloumn)
    # user = Student.objects.latest("id") # latest entry in Student table
    # print(user.id, user.stu_name,user.stu_city)
    # return HttpResponse(user)

    # # earliest(*fields/Coloumn)
    # user = Student.objects.earliest("id") # very first entry in this Student table
    # print(user.id, user.stu_name,user.stu_city)
    # return HttpResponse(user)

    # # exists()
    # user = Student.objects.all()
    # print(user.exists())
    # return HttpResponse(user)

    # # create(coloumn1=value1,coloumn2=value2)
    # user = Student.objects.create(stu_name='Ravi',stu_email='ravi@gmail.com',stu_city='Bhopal')
    # print(user.id, user.stu_name,user.stu_city)
    # return HttpResponse(user)

    # # get_or_create(default=None,**kwargs)
    # user,created = Student.objects.get_or_create(stu_name='RaviSingh',stu_email='ravisingh@gmail.com',stu_city='Pune')
    # print(user.id, user.stu_name,user.stu_city)
    # print(created)
    # return HttpResponse(user)

    ## update(**kwargs)
    # user = Student.objects.filter(id=1).update(stu_name='Ravi Thakur',stu_city='Indore')
    # print(user)
    # return HttpResponse(user)
    
    ## Update Multiple objects values at a time
    # user = Student.objects.filter(stu_city="Bhopal").update(stu_name='aditya')
    # print(user)
    # return HttpResponse(user)

    ## Delete the given object
    user = Student.objects.get(id=1).delete()
    # user = Student.objects.get(id=1)
    # user.delete()
    # user = Student.objects.filter(stu_name = "aditya").delete()
    # print(user)
    return HttpResponse(user)

    ## count all no of object prasent in table
    # user = Student.objects.all()
    # print(user.count()) # In terminal provide total no of objects present
    
    # user = Student.objects.explain()
    # print(user)

    # # update_or_create(**kwargs,default=None)
    # user,created = Student.objects.update_or_create(id=15, stu_city="Pune", defaults={'stu_name':"Ravi"})
    # print(user)
    # print(created)
    # return HttpResponse(user)