# Инструкции по запуску микросервиса

### 1. FastAPI микросервис в виртуальном окружение

Код сервиса находится в директории ```services```. Нужно перейти в данную директорию 

```
cd services
```

После нужно создать виртуальное окружение, активировать его и установить зависимости из ```requirements.txt```
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
...
