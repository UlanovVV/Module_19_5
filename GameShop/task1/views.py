from django.shortcuts import render
from .forms import UserRegister
from .models import *


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            users = Buyer.objects.value_list('name', flat=True)
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                info['message'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        users_info = Buyer.objects.all()
        users = [user.name for user in users_info]
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            info['message'] = f'Приветствуем, {username}!'
    return render(request, 'registration_page.html', info)


def platform_page(request):
    title = 'Лучшее описание игр!'
    page = "Главная страница"
    context = {
        'title': title,
        'page': page
    }
    return render(request, 'platform.html', context)


def card_page(request):
    title = 'Тут ты кое что узнаешь!'
    page = "Рубрика: 'А ты знал Чтоооо...'"
    context = {
        'title': title,
        'page': page
    }
    return render(request, "card.html", context)


def games_page(request):
    title = 'Игры игрульки'
    page = "Игры"
    context = {
        'title': title,
        'page': page,
        'games': Game.objects.all()
    }
    return render(request, 'games.html', context)

