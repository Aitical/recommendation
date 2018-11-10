from django.shortcuts import render
from django.core.paginator import Paginator
from api.models import Item_msg



def recommmendation(request,):
    pass




def index(request, page=1):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        user_ip = request.META['REMOTE_ADDR']
    msgs = Item_msg.objects.all()
    limit = 10
    paginator = Paginator(msgs, limit)
    items = paginator.page(page)
    page_num = paginator.num_pages
    if page == 1:
        pages = list(range(page, page+6))+[page_num]
    elif 6 < page < page_num-6:
        pages = [1]+list(range(page, page+6))+[page_num]
    else:
        pages = [1] + list(range(page-6, page))
    labels = ['Action', 'Adventure',
       'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama',
       'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance',
       'Sci-Fi', 'Thriller', 'War', 'Western']
    return render(request, 'layout.html', context={'items': items,
                                                   'pages': pages,
                                                   'current_page': page,
                                                   'recommendation': items,
                                                   'labels': labels})

