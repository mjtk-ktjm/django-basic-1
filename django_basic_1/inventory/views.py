from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

def index(request):
  # return HttpResponse('<p>In index view</p>')
  items = Item.objects.exclude(amount=0)
  return render(request, 'inventory/index.html', {
    'items': items,
  })


def item_detail(request, id):
  # return HttpResponse("Your item is {}".format(id))
  try:
    item = Item.objects.get(id=id)
  except Item.DoesNotExist:
    raise Http404('This item does not exist.')
  return render(request, 'inventory/item_detail.html', {
    'item': item,
  })

