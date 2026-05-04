from django.shortcuts import render
from .models import Order

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        qty = request.POST['quantity']

        Order.objects.create(name=name, quantity=qty)

        return render(request, 'index.html', {'msg': 'Order Saved!'})

    return render(request, 'index.html')