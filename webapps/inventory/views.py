from django.shortcuts import render

from inventory.forms import ItemForm
from inventory.models import Item

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

# Add a 
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

    # Display the add-item page if this is a 'GET' request
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
                    article_no=form.cleaned_data['article_no']
                    )
    new_item.save()

    return redirect(reverse('home'))

# delete the item
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)

    context = {}

    if request.method != 'POST':
        context['message'] = 'Deletes must be done using the POST method'
    else:
        item.delete()
        context['message'] = 'Item deleted.'

    return redirect(reverse('home'))
