# **Sales network**

Это проект, написанный на языках 

- Python 3.10.12

С использованием библиотек/фреймворков:
- Django 4.2.9
- Django REST framework 3.14.0
- drf-yasg 1.21.7
- PostgreSQL 16.2

Модель сети по продаже электроники, представленная с помощью веб-приложение, с API интерфейсом и админ-панелью. 

Сеть должна представлять собой иерархическую структуру из 3 уровней:
* Завод;
* Розничная сеть;
* Индивидуальный предприниматель. 

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). 
Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, 
т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные 
звенья - её уровень - 1.


## **Установка**
### Для установки проекта, следуйте инструкциям ниже:

**<p>1. Сделайте Fork этого репозитория. Репозиторий появится в ваших личных репозиториях на GitHub.</p>**

**1.1 Сделайте `git clone` форкнутого репозитория, чтобы получить репозиторий локально:**

**<p>2. Перейдите в папку с проектом.</p>**

**<p>3. Создайте и активируйте виртуальное окружение:</p>**

`python -m venv env`

`venv\Scripts\activate.bat
 - для Windows;`
`source venv/bin/activate
 - для Linux и MacOS.`

**<p>4. Установите зависимости проекта:</p>**

`pip install -r requirements.txt`

**<p>5. Создайте файл .env в корневой папке проекта и заполните данные для настройки переменных окружения. 
Также создайте файл .env.docker, чтобы внести туда соответствующие настройки для докера. Разница между этими двумя файлами будет заключается только в переменных:</p>**

`DB_HOST`

**<p>6. Примените миграции:</p>**

`python manage.py migrate`

**<p>7. ЗАПУСК BACKEND-ЧАСТИ: Запустите сервер:</p>**

`python manage.py runserver` или настройте запуск Django сервера в настройках.

Таким образом можно работать с backend-частью локально для отладки.

После установки проекта и запуска сервера вы сможете перейти на сайт 
[http://127.0.0.1:8000/redoc/ ](http://127.0.0.1:8000/redoc/)
(если сервер запущен локально), и начать пользоваться всеми API методами проекта.  

### Использование с помощью Docker
**<p>1. Создайте файл .env.docker в корневой папке проекта (sales_network/) и заполните данные для настройки проекта из файла .env.sample.docker:</p>**

**<p>2. ЗАПУСК BACKEND-ЧАСТИ: Воспользуйтесь командами:</p>**

`docker compose build` для создания оптимального билда проекта.

`docker compose up` для запуска docker compose контейнера.


## **Использование**
#### На проекте реализована регистрация новых пользователей через django админ-панель или API.
Также есть команда для создания суперпользователя `python manage.py create_su` с данными из .env файла

#### Для тестирования вы можете заполнить базу данных данными из фикстур при помощи команды `python manage.py fixturedata`

Либо создать свои через django админ-панель или API. 
Для поля network модели NetworkLink используются выбор из 3 вариантов:
* plant
* retail_network
* individual_entrepreneur


Через django админ-панель можно очистить задолженность перед поставщиками или перейти на страницу поставщика. (через API
обновление задолженности запрещено)

Использовать API могут только активные пользователи (флаг is_active)

Автор
TagRomEdu - qwertystyles@gmail.com
