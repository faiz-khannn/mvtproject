from django import forms

class empform(forms.form):
  empId= forms.IntegerField
  empName= forms.CharField(max_length=20)
  