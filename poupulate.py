
import os
os.environment.setdefault('DJANGO_SETTINGS_MODULE','newproject.settings')
import django
django.setup()
from testapp.models import student
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randiant(0,9))
    return int(num)
print(phonenumbergen())
def populate(n):
    for i in range(n):
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1,max=100)
        femail=fake.email()
        fphonenumber=phonenumbergen()
        faddress=fake.address()
        student_record=Student.objects.get_or_ create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
populate(100)        
