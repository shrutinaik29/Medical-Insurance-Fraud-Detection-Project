from django.core.management.base import BaseCommand
from myApp.models import MyModel  # Replace 'myapp' with your app name
import csv

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **options):
        with open('C:\\Users\\SUNIL\\OneDrive\\Desktop\\djnagoprj\\myProject\\myApp\\__pycache__\\data\\medical_aid_claims.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                obj = MyModel()
                obj.field1 = row['member_name']
                obj.field2 = row['email']
                obj.field3 = row['gender']
                obj.field4 = row['location']
                obj.field5 = row['employer']
                obj.field6 = row['relationship']
                obj.field7 = row['patient_name']
                obj.field8 = int(row['patient_suffix'])
                obj.field9 = row['patient_dob']
                obj.field10 = row['cause']
                obj.field11 = int(row['Fee_Charged'])
                obj.field12 = int(row['membership_period'])
                obj.field13 = int(row['number_of_claims'])
                obj.field14 = int(row['number_of_dependants'])
                obj.field15 = int(row['label'])
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
