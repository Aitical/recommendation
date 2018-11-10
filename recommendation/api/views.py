from django.shortcuts import render
from django.core.paginator import Paginator
from api.models import Item_msg, Item_labels
import pandas
import xgboost as xgb

USER_ITEM = xgb.Booster(model_file='./models/user_item.model')
USER_PERSON = xgb.Booster(model_file='./models/user_personal_label.csv.model')
ITEM_LABEL = xgb.Booster(model_file='./models/item_label.csv.model')



user_ips = {}

def recommmendation(model, labeldict):





def index(request, page=1):

    labels = [label.label for label in Item_labels.objects.all()]
    labeldict = {}
    for i in labels:
        labeldict[i] = 0

    if request.method == 'GET':
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            user_ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            user_ip = request.META['REMOTE_ADDR']

        if user_ip in user_ips:
            user_exit = False
        else:
            user_exit = False
            # user_ips[user_ip] = 'k'

        msgs = Item_msg.objects.all()

        movies = [msg.title.strip() for msg in msgs]

        limit = 10
        paginator = Paginator(msgs, limit)
        items = paginator.page(page)
        page_num = paginator.num_pages
        if page == 1:
            pages = list(range(page, page + 6)) + [page_num]
        elif 6 < page < page_num - 6:
            pages = [1] + list(range(page, page + 6)) + [page_num]
        else:
            pages = [1] + list(range(page - 6, page))

        return render(request, 'layout.html', context={'items': items,
                                                       'pages': pages,
                                                       'current_page': page,
                                                       'recommendation': items,
                                                       'user_exist': user_exit,
                                                       'movies': movies,
                                                       'labels': labels})
    elif request.method == 'POST':
        email = request.POST.get('email', '#')
        cheeck = request.POST.getlist('labels', None)
        person = request.POST.getlist('person', None)
        for i in cheeck:
            labeldict[i] = 1/len(cheeck)
        print(labeldict)

        return render(request, 'layout.html')


def select_by_label(request, label):
    pass