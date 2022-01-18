from django.shortcuts import render

from inventory.forms import ItemForm
from inventory.models import Item
from inventory.admin import download_csv

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse

# list all items
def home(request):
    if request.method == "GET":
        all_items = Item.objects.all().order_by("name")
        context = {'items': all_items}
        return render(request, 'homepage.html', context)

    context = {}
    return render(request, 'homepage.html', {})

# Add a new item
def item_page(request):
    context = {}

    # Display item page if this is a 'GET' request
    if request.method == 'GET':
        context['form'] = ItemForm()
        return render(request, 'item-page.html', context)
    
    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = ItemForm(request.POST)

    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'item-page.html', context)

    # If form data is valid. Add a new item.
    new_item = Item(name=form.cleaned_data['name'],
                    stock=form.cleaned_data['stock'],
                    article_no=form.cleaned_data['article_no'])
    new_item.save()

    return redirect(reverse('home'))

# delete an item
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        item.delete()

    return redirect(reverse('home'))

# edit an item
def edit_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'GET':
        context = { 'item': item, 
                    'form':ItemForm(initial={'name': item.name,
                                                'stock': item.stock,
                                                'article_no': item.article_no})}
        return render(request, 'edit-item.html', context)

    form = ItemForm(request.POST)
    if not form.is_valid():
        context = { 'item': item, 'form': form }
        return render(request, 'edit-item.html', context)

    item.article_no = form.cleaned_data['article_no']
    item.name = form.cleaned_data['name']
    item.stock = form.cleaned_data['stock']
    item.save()

    context = { 'item': item, 
                'form': form, 
                'message': 'Update Successfully'}
    return render(request, 'edit-item.html', context)

# source:
# https://stackoverflow.com/questions/18685223/how-to-export-django-model-data-into-csv-file/18689442
def export_csv(request):
  # Create the HttpResponse object with the appropriate CSV header.
  data = download_csv(request, Item.objects.all())
  response = HttpResponse(data, content_type='text/csv')
  return response