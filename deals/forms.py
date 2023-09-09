from .models import Deal
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ['deal_label', 'deal_message', 'created_at']
   
    # widgets = {
    #     "deal_label": TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Lable'
    #     }),
            
    #     "deal_message": Textarea(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Message'
    #     }),
            
    #     "created_at": DateTimeInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Date'
    #     })
    # }    
        
        