# Task Manager API

A scalable and maintainable FastAPI backend for task management with user authentication.
Designed with clean architecture, JWT-based security, and full CRUD support.

---

## Features
- **User Authentication** (JWT based)
  - Register, login, and `/auth/me` endpoint to fetch current user.
- **Task Management**
  - Create, list, update, and delete tasks.
  - Tasks are tied to the authenticated user (`owner_id`).
- **Database Integration**
  - PostgreSQL with SQLAlchemy ORM.
- **Testing**
  - Pytest suite with FastAPI’s `TestClient`.
- **Environment Config**
  - `.env` file support via Pydantic v2 `ConfigDict`.

---

## Tech Stack
- **FastAPI** – modern Python web framework
- **SQLAlchemy** – ORM for database models
- **PostgreSQL** – relational database
- **Pydantic v2** – data validation
- **Pytest** – testing framework
- **Alembic** - DB Migraton

---

## Project Structure
```
Task-Manager-API/
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── config.py        # Settings via Pydantic
│   ├── database.py      # DB session and engine
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── routers/
│       ├── auth.py      # Auth endpoints
│       └── tasks.py     # Task endpoints
├── tests/
│   └── test_app.py      # Pytest suite
├── requirements.txt
├── docker-compose.yml
└── README.md
```
---

## Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/harikrishna-goli/Task-Manager-API.git
   cd Task-Manager-API
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Start the Docker Desktop app

4. **Configure environment**
   Already a default `.env` given in the folder you can skip this step
   You can make to `.env` file if needed: 
   ```
   DATABASE_URL=postgresql+psycopg2://app_user:supersecret@localhost:5432/app_db
   JWT_SECRET=change_me
   JWT_ALG=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30

   DB_USER=app_user
   DB_PASSWORD=supersecret
   DB_NAME=app_db
   ```
5. **DB Migration**
    ```bash
    docker compose up -d
    alembic upgrade head
    ```

6. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## API Endpoints

### Auth
- `POST /auth/users/` → Register new user
- `POST /auth/login/` → Login and get JWT
- `GET /auth/me/` → Get current user

### Tasks
- `POST /tasks/` → Create task
- `GET /tasks/` → List tasks for current user
- `PUT /tasks/{task_id}` → Update task (title, description, status)
- `DELETE /tasks/{task_id}` → Delete task

---

## Testing
Run the test suite with:
```bash
pytest -v
```
