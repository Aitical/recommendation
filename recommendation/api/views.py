from django.shortcuts import render
from django.core.paginator import Paginator
from api.models import Item_msg

def index(request, page=1):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        user_ip = request.META['REMOTE_ADDR']
    msgs = Item_msg.objects.all()
    limit = 10
    paginator = Paginator(msgs, limit)
    items = paginator.page(page)
    print(items[0].id)
    return render(request, 'layout.html', context={'items': items})