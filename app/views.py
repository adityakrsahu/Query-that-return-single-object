from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    
     # latest(*fields/Coloumn)
    user = Student.objects.latest("id") # latest entry in Student table
    print(user.id, user.stu_name,user.stu_city)
    return HttpResponse(user)

    # earliest(*fields/Coloumn)
#     user = Student.objects.earliest("id") # very first entry in this Student table
#     print(user.id, user.stu_name,user.stu_city)
#     return HttpResponse(user)

#     # exists()
#     user = Student.objects.all()
#     print(user.exists())
#     return HttpResponse(user)

#   # update(**kwargs)
#     user = Student.objects.filter(id=1).update(stu_name='Ravi Thakur',stu_city='Indore')
#     print(user)
#     return HttpResponse(user)


## Update Multiple objects values at a time
    # user = Student.objects.filter(stu_city="Bhopal").update(stu_name='Neeraj')
    # print(user)
    # return HttpResponse(user)

    ## Delete the given object
    # user = Student.objects.get(id=14).delete() or
    # user = Student.objects.get(id=14)
    # user.delete()
    # user = Student.objects.filter(stu_name = "Neeraj").delete()
    # print(user)
    # return HttpResponse(user)

    ## count all no of object prasent in table
    # user = Student.objects.all()
    # print(user.count()) # In terminal provide total no of objects present
    
    # user = Student.objects.explain()
    # print(user)


#     last()
#     user = Student.objects.last()
#     # user = Student.objects.order_by('stu_name').last()
#     # user = Student.objects.order_by('-stu_name').last()
#     print(user.id, user.stu_name,user.stu_city)
#     return HttpResponse(user)


     # first()
#     user = Student.objects.first()
#     # user = Student.objects.order_by('stu_name').first()
#     # user = Student.objects.order_by('-stu_name').first()
#     print(user.id, user.stu_name,user.stu_city)
#     return HttpResponse(user)







        # user = Student.objects.create(stu_name='ajay',
        #                               stu_email='ajay@gmail.com',
        #                               stu_contact='4561237',
        #                               stu_city='chakhaji')
        # # print("data cretat")
        # return HttpResponse(user)

        # user=Student.objects.first()
        # return HttpResponse(user)

        # user=Student.objects.get(id=5)
        # print(user.id,user.stu_name,user.stu_email,user.stu_contact,user.stu_city)
        
        # return HttpResponse(user)















































        
    

        # user = Student.objects.get(id=5)

        # print(user.id,user.stu_name,user.stu_email,user.stu_contact,user.stu_city)
        # user = Student.objects.get(stu_city = 'bhopal')
        # user = Student.objects.get(stu_city = 'bihar')
        # user = Student.objects.order_by('-stu_name').first()

        # return HttpResponse(data)

        # user = Student.objects.get(stu_city = 'bhopal')
        # user = Student.objects.get(stu_city = 'bihar')
        # user = Student.objects.order_by('-stu_name').first()

        # return HttpResponse(user)


      
    