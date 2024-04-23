# referal-for-hummer-systems

Простая реферальная система с имитацией подтверждения по номеру телефона (Отсутсвует поддержка проверки на символы ввода номера телефона)

- Используемые технологии:
- + Docker
  + Docker Compose
  + Django 3.2.0
  + Postgress
  + Django Cors Header 3.1.0
  + Django Rest Framework 3.12.4
  + Django Rest Framework Simple JWT 4.8.0
  + Nginx
  + Bootstrap 4.0
  + Jquery 3.6

    Установка:
    - Сделать клон репозитория на локальную либо серверную машину
    - Запустить команды:
    - + docker-compose up -d --build
      + docker-compose run app python3 manage.py migrate
      + docker-compose run app python3 manage.py createsuperuser
    - В settings.py в поле ALLOWED_DOOMAIN прописать необходимый хост.

    ------------------------------------------------------------------

    API:
    
      
