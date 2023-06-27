from django.contrib.auth.models import *
from django.db import models
from django import forms
import csv

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.EmailField()


def load_data_from_csv():
    with open('C:\\Users\\SUNIL\\OneDrive\\Desktop\\djnagoprj\\myProject\\myApp\\__pycache__\\data\\medical_aid_claims.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create an instance of your model and set its attributes
            obj = MyModel()
            member_name = models.CharField(max_length=100)
            email = models.EmailField(max_length=254)
            gender = models.CharField(max_length=100)
            location = models.CharField(max_length=100)
            employer = models.CharField(max_length=100)
            relationship = models.CharField(max_length=100)
            patient_name = models.CharField(max_length=100)
            patient_suffix = models.IntegerField()
            patient_dob = models.DateField(date_format='%m-%d-%Y')
            cause = models.CharField(max_length=100)
            Fee_Charged = models.IntegerField()
            membership_period = models.IntegerField()
            number_of_claims = models.IntegerField()
            number_of_dependants = models.IntegerField()
            label = models.IntegerField()
            # Set more fields as needed
            obj.save()
