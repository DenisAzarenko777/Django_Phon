from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    phone_query = request.GET.get('sort')
    if phone_query == 'name':
        phone = Phone.objects.order_by('name')
    elif phone_query == 'min_price':
        phone = Phone.objects.order_by('price')
    elif phone_query == 'max_price':
        phone = Phone.objects.order_by('-price')
    else:
        phone = Phone.objects.all()
    context = {'Phoness': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone = Phone.objects.filter(slug=slug)
    phone_filter = request.GET.get('slug')
    context = {'Phoness': phone}
    return render(request, template, context)
