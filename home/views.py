from django.shortcuts import render,redirect
from .models import RestaurantInfo,ContactForm
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'success':'Thank you for your message! We will ve in touch with my orders!'
            'submission': serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
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


from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListAPIView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializers_class = MenuCategorySerializer
    
