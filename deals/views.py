from django.shortcuts import render, redirect, get_object_or_404
from .models import Deal
from .forms import DealForm
from django.views.generic import DeleteView
    
def index(request):
    error = ''
    if request.method == 'POST':
        form = DealForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/deals/')
        else:
            error = "Неверная форма"
            
    deals = Deal.objects.all()
    
    form = DealForm()
    
    date = {
        'deals': deals,
        'form': form,
        'error': error,
    }
    
    search_title = request.GET.get('search_title', '') # Поиск
    if search_title:
        deals = deals.filter(deal_label__icontains=search_title)
        
    return render(request, 'deals/index.html', date)

def delete_deal(request, deal_id):
    deal = get_object_or_404(Deal, id=deal_id)
    deal.delete()
    return redirect('/deals/')


def update_deal(request, deal_id):
    deal = get_object_or_404(Deal, id=deal_id)
    
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('/deals/')
    else:
        form = DealForm(instance=deal)
    
    return render(request, 'deals/index.html', {'form': form})
