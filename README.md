
- Монтаж env
```shell
python -m virtualenv env

source env/bin/activate
```

- Установка зависимостей
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Запуск как разработчик
```shell
export FLASK_ENV='development'
```

- У меня без flask run не работает, так что:
```shell
export FLASK_APP=run.py
```

- Создание моделей (очистит БД и создаст все модели, указанные в импорте)
```shell
python create_tables.py
```

- Загрузка данных в базу
```shell
python load_fixture.py
```
Скрпит читает файл fixtures.json и загружает данные в базу. Если данные уже загружены - выводит соответсвующее сообщение. 

- Запуск с фронтэндом
```shell
flask run -h localhost -p 25000
```

