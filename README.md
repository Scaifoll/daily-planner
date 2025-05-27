# Daily Planner API

## Описание
Backend-приложение ежедневника на FastAPI с CRUD-функциональностью.

## Возможности
- Создание задачи
- Получение списка задач
- Получение задачи по ID
- Обновление задачи
- Удаление задачи
- Отметка задачи как отработанной

## Запуск

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload or py uvicorn app.main:app --reload
```

## Миграции

```bash
alembic init alembic
# Указать путь к metadata в alembic/env.py:
# from app.database import Base
# target_metadata = Base.metadata

alembic revision --autogenerate -m "Initial"
alembic upgrade head
```

## Документация
После запуска: [http://localhost:8000/docs](http://localhost:8000/docs)
