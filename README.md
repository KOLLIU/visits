# visits

### Протестировать проект можно по адресу 51.250.109.231
login: admin\
password: admin

##### GET: /api/sale_point_list (phone=89163205020)
##### POST: /api/make_visit ({"phone": 89163205020, "sale_point_pk": 1, "latitude": 100, "longitude": 100})

### Запуск проекта
Необходимые зависимости указаны в requirements.txt\
Данные для входа в БД (PostgreSQL) находятся в файле main/main/.env\
Перед запуском проекта необходимо выполнить **collectstatic**
