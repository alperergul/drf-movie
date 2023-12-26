# Django Komutları

## Proje oluşturma

```command
django-admin startproject <<project_name>>
python manage.py startapp watchlist_app
```

## Proje Çalıştırma

```command
python manage.py runserver
```

- Bu komuttan sonra sqlite3 oluşturulur. Ve 18 tane migration hatası gözükür.

## Migrate

- Bu komut ile migrationlar oluşturulur.

- Migrationsları oluşturmak için

```command
ptyhona manage.py makemigrations
```

-Migraitonları işlemek için

```command
python manage.py migrate
```

- Migrationlar işlendikten sonra tekrar superuser create etmemiz gerekebilir.

## Super User Create

```command
python manage.py createsuperuser
```
