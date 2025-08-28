from django import forms
from .models import Feedback,ContactSubmission

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments']
        widgets = {
            'comments':forms.Textarea(attrs={
                'row':6,
                'placeholder':'Leave your feedback here...',
                'class':'form-control'
            }),
        }

class ContactForm(forms.ModelForm):
    """
    A Django model form for the ContactSubmissions model.
    """
    class Meta:
        model = ContactSubmission
        fields = ['name','email']

        