

pip3 install virtualenv # Установка библиотеки для создния виртуального окружения

python3 -m venv venv # Создание виртуального окружения

source venv/bin/activate # Вход в виртуального окружение (linux)

# Устанавливаем необходимые библиотеки 
pip3 install Django==3.2 # фремйворк джанго

pip3 install djangorestframework==3.12.4 # приложение для rest api

pip3 install drf-yasg==1.21.4 # приложение для автоматического создания сваггера

django-admin startproject pairwase_sum # создание проекта

python3 manage.py startapp api # создание приложения (внутри папки проекта)



По окончанию работы с проектом выходим из виртуального окружения в директории, где лежит папка venv

deactivate

Документация на тему:

https://docs.djangoproject.com/en/3.2/

https://www.django-rest-framework.org/

https://drf-yasg.readthedocs.io/en/stable/