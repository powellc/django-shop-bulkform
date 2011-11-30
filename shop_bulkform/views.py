from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from shop.models.productmodel import Product
from shop.util.cart import get_or_create_cart
from django.views.generic import ListView
from datetime import date

class CartBulkView(ListView):
    ''' An addon view for django-shop to allow bulk adding to the cart. '''

    model = Product
    template_name='shop/order_bulk_form.html'
    action=None

    def post(self, *args, **kwargs):
        """
        This is to *add* items in bulk to the cart. Optionally, you can pass it
        quantity parameters to specify how many you wish to add at once (defaults
        to 0)
        """
        qty_field_prefix = 'add_item_quantity-'
        qty_fields = [k for k in self.request.POST.keys()
                if k.startswith(qty_field_prefix)]
        cart_object = get_or_create_cart(self.request)

        for key in qty_fields:
            id = key[len(qty_field_prefix):]
            product = Product.objects.get(pk=id)
            if int(self.request.POST[key]) > 0:
                cart_item = cart_object.add_product(product, int(self.request.POST[key]))
                cart_object.save()
        return HttpResponseRedirect(reverse('cart'))
