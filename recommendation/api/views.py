from django.shortcuts import render
from django.core.paginator import Paginator
from api.models import Item_msg, Item_labels, Item_label, User_label, User_item
import pandas as pd
import xgboost as xgb

USER_ITEM = xgb.Booster(model_file='./models/user_item.model')
USER_PERSON = xgb.Booster(model_file='./models/user_personal_label.csv.model')
ITEM_LABEL = xgb.Booster(model_file='./models/item_label.csv.model')



user_ips = {}


def recommmendation(model, labeldict):
    test = pd.DataFrame(labeldict, index=[0])
    test = xgb.DMatrix(test)
    if model == 'user_item':

        label = USER_ITEM.predict(test)[0]
        users = [user.user_id for user in User_label.objects.filter(user_id=int(label))]
        items = [item.item_id for item in User_item.objects.filter(user_id__in=users)]
        return items
    elif model == 'user_person':
        label = USER_PERSON.predict(test)[0]
    else:
        label = ITEM_LABEL.predict(test)[0]

def sort_and_random_item(items):

    res = Item_msg.objects.order_by('hot_point').filter(item_id__in=items)
    return res



def index(request, page=1):

    labels = [label.label for label in Item_labels.objects.all()]
    labeldict = {}
    for i in labels:
        labeldict[i] = 0
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        user_ip = request.META['REMOTE_ADDR']

    limit = 10
    msgs = Item_msg.objects.all()
    movies = [msg.title.strip() for msg in msgs]
    paginator = Paginator(msgs, limit)
    items = paginator.page(page)
    page_num = paginator.num_pages
    r_items = items
    if user_ip in user_ips:
        user_exit = True
        item_ids = user_ips[user_ip]
        r_items = sort_and_random_item(item_ids)[:10]

    else:
        user_exit = False


    if page == 1:
        pages = list(range(page, page + 6)) + [page_num]
    elif 6 < page < page_num - 6:
        pages = [1] + list(range(page, page + 6)) + [page_num]
    else:
        pages = [1] + list(range(page - 6, page))

    if request.method == 'POST':
        email = request.POST.get('email', '#')
        cheeck = request.POST.getlist('labels', None)
        person = request.POST.getlist('person', None)
        for i in cheeck:
            labeldict[i] = 1/len(cheeck)

        item_ids = recommmendation('user_item', labeldict)
        user_ips[user_ip] = item_ids
        user_exit = True
        r_items = sort_and_random_item(item_ids)[:10]


        return render(request, 'layout.html', context={'items': items,
                                                       'pages': pages,
                                                       'current_page': page,
                                                       'recommendation': r_items,
                                                       'user_exist': user_exit,
                                                       'movies': movies,
                                                       'labels': labels})
    if request.method == 'GET':



        return render(request, 'layout.html', context={'items': items,
                                                       'pages': pages,
                                                       'current_page': page,
                                                       'recommendation': r_items,
                                                       'user_exist': user_exit,
                                                       'movies': movies,
                                                       'labels': labels})



def select_by_label(request, label):
    pass