from django.shortcuts import render

def base(request):
    return render(request, r".\app\templates\base.html")

def child1(request):
    return render(request, r".\app\templates\child1.html")

def child2(request):
    return render(request, r".\app\templates\child2.html")
