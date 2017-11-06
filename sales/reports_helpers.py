from .models import *
from .variables import ROUND_DIGITS

from collections import OrderedDict

def return_round_or_emtpy_string(num, digits=2):
    try:
        return round(num, digits)
    except TypeError:
        return ''

def get_pricelist_price_data(pricelist, include_cost=False):
    '''return a list of ordered dicts with price-data:
    - sku
    - rrp
    - per 1
    - per 6
    - per 12
    - per 48
    '''
    data = []
    for item in pricelist.pricelistitem_set.filter(product__active=True).order_by('product__sku'):
        d = OrderedDict()
        d['sku'] = item.product.sku
        d['name'] = '{}\n{}'.format(item.product.name, item.product.product_model.size_description)

        d['RRP'] = return_round_or_emtpy_string(item.rrp)
        d['per 1'] = return_round_or_emtpy_string(item.per_1)
        d['per 6'] = return_round_or_emtpy_string(item.per_6)
        d['per 12'] = return_round_or_emtpy_string(item.per_12)
        # d['per 48'] = return_round_or_emtpy_string(item.per_48)

        try:
        	d['stock'] = int(item.product.available_stock)
        except ValueError:
        	d['stock'] = 0

        if include_cost:
            d['cost'] = round(item.product.cost, ROUND_DIGITS)
        data.append(d)
    return data

def get_transport_costs():
    countries = list(set([i.country for i in PriceTransport.objects.all()]))
    headers = ('Country', 'Transport cost', 'Free from')
    data = []
    data.append(headers)

    for c in countries:
        try:
            free = PriceTransport.objects.filter(country=c, shipping_price=0.0)[0] #.order_from_price
            paying = PriceTransport.objects.filter(country=c).order_by('-order_from_price').exclude(id=free.id)[0]
        except IndexError:
            free = ''
            paying = PriceTransport.objects.filter(country=c).order_by('-order_from_price')[0]
        data.append((free,paying))

    return data
