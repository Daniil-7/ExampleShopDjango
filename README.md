# Интерент-магазин на Django

## Описание

### Внимание! Для лучшеего понимания как выглядит проект посмотрите на [пример](https://exampleshopdjango.herokuapp.com/)

Полноценый самописный интернет магазин написаный на django. 

### Возможности магазина

1. Создание товара
2. Создание категорий и настройка их ирерархии
3. Создание событий и аккций
4. Написание в службу поддержки(почту или почты которые вы укажите в настройках)
5. Написание мини статей
6. Корзина с возможностью оплатить
7. Возможность оставлять отзыв(для зарегистрированых пользователей)
8. Изменение данных юзера через профиль
9. Регистрация и система входа с возможностью востановить пороль через почту.
10. Поиск товара
11. Создание скидок

## Инструкция по установке:

### Предварительная настройка

#### Настройка cloudinary

1. Регистрируемся на [cloudinary](https://cloudinary.com/)
2. Переходим в "Dashboard"
3. В файле diplom_django_netology/configure.py и вствляем в переменые свои данные под коментарием cloudinary

#### Настройка gmail(или другой почты)

1. Сначало нужно установить [Двухэтапную аутентификацию](https://myaccount.google.com/signinoptions/two-step-verification) 
2. Затем сгенирировать [пароль для сайта](https://myaccount.google.com/apppasswords)
3. в файле diplom_django_netology/configure.py заполнняем данные под комментарием mail

#### Настройка fondy(оплаты)(Данный пункт не обязателен пока вы не захотите подключить оплату(тестовый режим))

1. Регистрируемся на [fondy](https://fondy.io/gb/)
2. в файле diplom_django_netology/configure.py заполнняем данные под комментарием fondy(cloudipsp)

### Установка:

 1. Установите зависимости:
```sh
python pip install -r requirements.txt
```
2. Выполните миграции:
```sh
python manage.py makemigrations
python manage.py migrate
```
3. Создание супер юзера
```sh
python manage.py createsuperuser
```
4. Запустите тестовый сервер:
  ```sh
 python manage.py runserver --settings=settings.local
 ```
5. Перейдите по ссылке: (http://127.0.0.1:8000)

6. При диплои используете:
  ```sh
 python manage.py runserver
 ```
