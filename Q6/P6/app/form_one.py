from django import forms

class my_Form(forms.Form):
    name = forms.CharField(label = "Enter your member ID: ", max_length = 20)
    email_add = forms.EmailField(label = "Enter your e-mail ID: ")
    course = forms.CharField(label = "Enter your course: ", max_length = 20)
    check = forms.BooleanField(label = "Staff")
