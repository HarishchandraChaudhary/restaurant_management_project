from django.shortcuts import render

def home_page_view(request):
    return render(request,'home/index.html')


def about(request):
    return render(request,'home/about.html')

def _404(request):
    return render(request,'template/404.html')