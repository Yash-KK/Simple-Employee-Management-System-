# from cProfile import label
from django import forms
from phonenumber_field.formfields import PhoneNumberField
class AddEmp(forms.Form):
    f_name = forms.CharField(max_length=100,label="First Name")
    l_name = forms.CharField(max_length=100,label="Last Name")
    dept = forms.IntegerField(min_value=1,max_value=6,label="Department")
    salary = forms.IntegerField(label="Salary")
    bonus = forms.IntegerField(label="Bonus")
    role = forms.IntegerField(min_value=1,max_value=8,label="Role")
    phone = forms.IntegerField()
    

   
