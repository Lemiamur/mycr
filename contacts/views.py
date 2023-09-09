from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import DeleteView
    
def index(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/contacts/')
        else:
            error = "Неверная форма"
            
    contacts = Contact.objects.all()
    
    form = ContactForm()
    
    date = {
        'contacts': contacts,
        'form': form,
        'error': error,
    }
    
    search_title = request.GET.get('search_title', '') # Поиск
    if search_title:
        contact = contact.filter(Name__icontains=search_title)
        
    return render(request, 'contacts/index.html', date)

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('/contacts/')


def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/contacts/')
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contacts/index.html', {'form': form})
