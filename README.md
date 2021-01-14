# Древовидное меню

## 1. Описание
Древовидное меню с использование Django и template tags. Реализовано 3 уровня вложенности, начиная с родительского меню. Меню создаются в админской панели, для отрисовки созданного меню нужно добавить в файл [home.html](menu_app/templates/home.html):
```python
{% draw_menu 'slug' %}
```
гдe slug - это соответствующее поле модели в админской панели.

### Первоначальный вид домашней страницы

![home-page](https://sun9-3.userapi.com/impf/a77KWEFRSp7XXm2l8jGvyBs2HDLSjoT8npZi7Q/Uo6RPPlu5Gk.jpg?size=1280x228&quality=96&sign=aa80e27e6a0ddc4ab7413d50edbb0c29&type=album)

## 1. Установка

```bash
pip install pipenv
git clone https://github.com/grum261/tree-menu
cd tree-menu
pipenv install
pipenv shell
cd menu_app
python manage.py runserver
```

## 2. Добавление собственного меню

### 2.1 Создаем суперпользователя
```bash
python manage.py createsuperuser
```
### 2.2 Заходим в админскую панель http://127.0.0.1:8000/admin/ и добавляем родительское меню
![](https://sun9-13.userapi.com/impf/EGCVVfLOp4ctnkOTQj74ap9j_jXcsQlur6BnLQ/8uc5ExV4OqI.jpg?size=1280x418&quality=96&sign=3e4c7e6e1a90293088cc23ba618faed7&type=album)

### 2.3 Добавляем template tag для отрисовки меню
[home.html](menu_app/templates/home.html)
```python
{% extends 'base.html' %}
{% load draw_menu %}

{% block content %}
    {% draw_menu 'home' %}
    {% draw_menu 'products' %}
    {% draw_menu 'settings' %} #Наше новое меню 
    {% draw_menu 'contacts' %}
{% endblock %}
```
