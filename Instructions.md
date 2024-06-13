# Инструкции по запуску микросервиса

Код сервиса находится в директории ```services```. Нужно перейти в данную директорию 

```
cd services
```

### 1. FastAPI микросервис в виртуальном окружение


Для начала нужно создать виртуальное окружение, активировать его и установить зависимости из ```requirements.txt```
```
python3 -m venv ./venv
source venv/bin/activate
pip3 intall -r requirements.txt
```

После установки зависимостей можно запустить сервис командой:

```
uvicorn main:app --host 0.0.0.0 --port 4555
```

Пример запроса:
```
curl -X 'POST' \
  'http://localhost:4555/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "123",
  "params_model": {
    "floor": 0,
    "kitchen_area": 0,
    "living_area": 0,
    "rooms": 0,
    "is_apartment": true,
    "studio": true,
    "total_area": 0,
    "build_year": 0,
    "building_type_int": 0,
    "latitude": 0,
    "longitude": 0,
    "ceiling_height": 0,
    "flats_count": 0,
    "floors_total": 0,
    "has_elevator": true
  }
}'
```

### 2. FastAPI микросервис в Docker-контейнере

Нужно для начала создать файл ```.env``` в котором будут указаны порт и автор в параметрах ```APP_PORT``` и ```AUTHOR``` соответсвенно.


Теперь нужно собрать образ с помощью команды:
```
docker image build . -f Dockerfile_ml_service --tag fastapi_service:v1
```

После запускаем контейнер командой:
```
docker container run --publish 4555:4555 --env-file .env --volume=./models:/app/models  fastapi_service:v1
```


Запуск контейнера с помощью docker compose:
```
docker compose up --build
```

### Этап 3. Запуск сервисов для системы мониторинга

Для начала нужно добавить в файл ```.env``` переменные ```GRAFANA_USER``` и ```GRAFANA_PASS``` с именем пользователя и паролем.

После запустить все с помощью команды:
```
docker compose up --build
```