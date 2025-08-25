from django import forms
from .models import Feedback

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