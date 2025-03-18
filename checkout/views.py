from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R3pGaBTORn4q2dgV0AqTIyy1eevSDv4omVvWYH5RsA91PB8p4QnS5PNBinLRkmkRS7RusAizvLdYs27gka8h2Qt00ABjB0JaH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)