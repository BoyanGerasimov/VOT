# Магазинско приложение с Docker

Това е просто магазинско приложение, което позволява управление на продукти в магазин. Можете да добавяте, премахвате и изброявате продукти, като използвате PostgreSQL като база данни. Това приложение е контейнеризирано с Docker за лесна настройка и изпълнение.

## Преимуществени условия

Уверете се, че имате инсталирани следните инструменти:

- **Docker**: [Инсталирайте Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Инсталирайте Docker Compose](https://docs.docker.com/compose/install/)
- **PostgreSQL**: [Инсталирайте PostgreSQL](https://www.postgresql.org/download/)

## Стъпки за стартиране на приложението

### 1. Клонирайте хранилището

#### Клонирайте това хранилище на локалната си машина:

 ```bash
 git clone https://github.com/your-username/shop-app.git
 cd shop-app
```
### 2. Изградете и стартирайте контейнерите
```bash
docker-compose up -d --build
```
### 3. Присъединете се към контейнера shop_app
 ```bash
docker exec -it shop_app /bin/bash
```
### 4. Стартирайте Python приложението
 ```bash
python app.py
```

### 5. Спиране на контейнерите
 ```bash
docker-compose down
```