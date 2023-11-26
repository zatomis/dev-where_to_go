# Интерактивная карта Москвы

Этот проект - интерактивная карта Москвы, где пользователи могут просматривать различные виды
активного отдыха с подробными описаниями и комментариями. 

Дополнительные функции - добавляются администратором вручную через.

## Установка при развертывании проекта локально

Для установки проекта, выполните следующие шаги:

1. Склонируйте репозиторий:
```bash
git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
```
2. Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv env
source env/bin/activate
```
Работоспособность проекта протестирована на python 3.10
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Создайте файл .env и заполните в нем следующие переменные:
```
SECRET_KEY=<YOUR SECRET KEY>
DEBUG=True
```
## Использование (локально)

Для интерфейса администратора нужно создать суперпользователя. Для этого выполните команду:
```bash
python manage.py createsuperuser
```
Затем запустите сам сервер
```bash
python manage.py runserver
```
В браузере и перейдите по адресу http://localhost:8000/ для просмотра интерактивной карты Москвы.
Добавление или изменение локаций, происходит в режиме администратора по ссылке: http://localhost:8000/admin.

**Интерфейс администратора позволяет:**

1. Просмотреть список локаций и найти локацию по названию.
2. Перейти на страницу редактирования локации где можно обновить описание. Добавить новые картинки или удалить старые, а также переместить их в начало списка, чтобы изменить порядок их отображения на сайте.
3. Добавить новые локации или удалить старые

## Пример данного проекта на www.pythonanywhere.com
Перейдите по ссылке, для просмотра действующего проекта 
www.zatomis.pythonanywhere.com


## Цели проекта

Код написан в учебных целях — курс по Python и веб-разработке на сайте [Devman](https://dvmn.org).
