from django.shortcuts import render,redirect
from .models import RestaurantInfo,ContactForm

def home(request):
    try:
        info = RestaurantInfo.objects.get(pk=1)
        restaurant_name = "Our Restaurant "

        context = {
            'restaurant_name':restaurant_name
        }
        return render(request,'templates/homepage.html')
def contact(request):
    """
    Handles the contact form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        else:
            form = ContactForm()
        return render(request,'templates/contact.html',{'form':form})