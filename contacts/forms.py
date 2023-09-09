from .models import Contact
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['Name', 'Phone', 'Message', 'Email', 'created_at']