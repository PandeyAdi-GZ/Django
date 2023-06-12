from django.shortcuts import render
from .form_one import my_Form

def index(request):
    context = {}
    context["form"] = my_Form()
    form = my_Form(request.POST)
    if form.is_valid():
        Member_ID = form.cleaned_data["name"]
        emailvalue = form.cleaned_data["email_add"]
        course_id = form.cleaned_data["course"]
        chk = form.cleaned_data["check"]
        print("This is member ID: ",Member_ID)
        print("This is e-mail address: ",emailvalue)
        print("This is course name: ",course_id)
        print("This is status of staff: ",chk)

    return render(request, r".\app\templates\first_form.html", context)