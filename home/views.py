from django.shortcuts import render

def home_page_view(request):
    return render(request,'home/index.html')


def about(request):
    return render(request,'home/about.html')