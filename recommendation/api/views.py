from django.shortcuts import render


def index(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        user_ip = request.META['REMOTE_ADDR']
    print(user_ip)
    return render(request, 'layout.html', context={'ip': user_ip})