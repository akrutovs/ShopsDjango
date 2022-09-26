# Тестовое задние Python (backend)
## Крутов Алексей
### Описание функционала:
#### Запросы (HTML страница):
1. GET /city/ - получение списка всех городов базы данных
2. GET /city/{city_id}/street - получение всех улиц города
3. GET /shop/ - получение всех магазинов

#### Запросы (JSON формат):
1. GET /api/v1/city/ - получение списка всех городов базы данных
2. GET /api/v1/city/{city_id}/street - получение всех улиц города
3. GET /api/v1/shop/ - получение всех магазинов 
4. POST /api/v1/shop/ - Принимает JSON со следующими параметрами
```sh
{
    "city": "Название_города",
    "street": "Название_улицы",
    "name": "Имя_магазина",
    "start_time": "Часы_открытия 0:00",
    "end_time": "Часы_закрытия 0:00"
}
```
5. GET /api/v1/shop/?street=&city=&open=0/1 - получение всех магазинов с параметрами 
фильтрации (по улице, городу, открыт ли магазин в данный момент)

## Инструкция по установке:

### Docker установка:

1. Если у вас не установлен Docker: Установите [Docker,docker-compose](https://docs.docker.com/get-docker/).
2. Склонируйте репозиторий
```sh
git clone https://github.com/akrutovs/ShopsDjango.git
```
3. Перейдите в каталог проекта и запустите контейнеры:
```sh
docker-compose up --build -d
```
4. Выполните миграции
```sh
docker-compose run web python manage.py migrate
```
5. Создайте супер пользователя для работы с admin панелью
```sh
docker-compose run web python manage.py createsuperuser
```
6. Перейдите по ссылке: (http://127.0.0.1:8000) для взаимодействия с приложением
7. Перейдите по ссылке: (http://127.0.0.1:8080) для взаимодействия с базой данных (база данных postgresql username=postgres, password=postgres,name_database=database)