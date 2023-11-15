from django.shortcuts import render


def index_page(request):
    return render(request, 'index.html', context={'user': {'is_authorised': False}, 'items': range(1, 7)})

def login_page(request):
    return render(request, 'login.html', context={'user': {'is_authorised': False}})

def register_page(request):
    return render(request, 'register.html', context={'user': {'is_authorised': False}})

def question_page(request, id):
    return render(request, 'question_page.html', context={'user': {'is_authorised': True}})

def ask_page(request):
    return render(request, 'ask.html', context={'user': {'is_authorised': True, 'name': 'George'}})

def settings_page(request):
    return render(request, 'settings.html', context={'user': {'is_authorised': True, 'name': 'George',
                                                              'login': 'cheater@gmail.com'}})
