from django.shortcuts import render

def default_view(request):
    return render(request, 'tax_app/default.html')

def calculate_price(request, num):
    tax_rate = 0.15
    total_price = float(num) * (1 + tax_rate)
    context = {'total_price': total_price}
    return render(request, 'tax_app/price.html', context)

def tax_rate_view(request):
    tax_rate = 0.15
    context = {'tax_rate': tax_rate}
    return render(request, 'tax_app/tax_rate.html', context)
