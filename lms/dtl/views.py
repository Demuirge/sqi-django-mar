from django.shortcuts import render

# Create your views here.

def cart(request):
    context = {
        'user': "Timothy Okonkwo",
        'cart_items': ["tomato", "strawberry", "vanilla ice cream", "burger", "cake"],
        'is_favorite': True,
        'no_of_items_in_cart': 5
    }
    return render(request, 'dtl/syntax.html', context)
