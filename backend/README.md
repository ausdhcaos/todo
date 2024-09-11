## DBs

- Install docker
- `docker compose -f docker-compose-dev.yml up --detach`

## INIT
- `python -m venv .venv`
- `source .venv/bin/activate`
- `pip install poetry`
- `poetry install`
- `alembic upgrade head` to create tables in your local db

## Dev
- `source .venv/bin/activate`
- `uvicorn main:app --reload`

## Migration

### Autogenerate a new migration

```
alembic revision --autogenerate -m "new migration"
```

### Apply the migration

```
alembic upgrade head
```

### Generate sql

#### Generate single version

```
alembic upgrade f4e28cb05547 --sql
```

#### Generate multiple version (Exclude the beginning version)

```
alembic upgrade c104339725db:c104339725db --sql
```
