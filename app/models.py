from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name =models. CharField(max_length=50)
    stu_email =models. CharField(max_length=50)
    stu_contact =models. CharField(max_length=50)
    stu_city =models. CharField(max_length=50)



    class Meta:
        db_table = 'Student'
        verbose_name_plural = 'Student'  #  student change ho jata hai

    def __str__(self):
        return self.stu_name
        # return self.stu_email
        # return self.stu_contact