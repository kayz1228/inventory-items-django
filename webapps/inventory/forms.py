from inventory.models import Item
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'article_no', 'stock')
        widgets = {
            'name': forms.TextInput(attrs = {
                'id': 'id_item_name',
                'rows': '1'}),
            'article_no': forms.TextInput(attrs = {
                'id': 'id_article_number',
                'rows': '1'}),
            'stock': forms.NumberInput(attrs = {'id' : 'id_item_stock'})
        }
    
    # Form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        article_no = cleaned_data.get('article_no')
        stock = cleaned_data.get('stock')

        if not name:
            raise forms.ValidationError("You must enter item name.")
        if not article_no:
            raise forms.ValidationError("You must enter article number of this item.")
        if not stock:
            raise forms.ValidationError("You must enter stock of the item.")

        return cleaned_data
    
    # Form validation for the article number field.
    def clean_article_no(self):
        article = self.cleaned_data.get('article_no')
        if Item.objects.filter(article_no=article):
            raise forms.ValidationError("Item article number already exists.")

        # Return the cleaned data got from the cleaned_data dictionary
        return article