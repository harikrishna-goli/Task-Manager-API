
---

## 🚀 Core Framework & Server
- **FastAPI** → The main web framework. Lets you build APIs quickly with automatic validation, async support, and interactive docs (Swagger/OpenAPI).
- **uvicorn[standard]** → ASGI server that runs your FastAPI app. The `[standard]` extra installs useful performance dependencies (like `uvloop`, `httptools`).

---

## 🗄️ Database & Migrations
- **SQLAlchemy** → ORM (Object Relational Mapper). Lets you define Python classes (`models`) that map to database tables, and query them elegantly.
- **Alembic** → Migration tool for SQLAlchemy. Tracks schema changes (new tables, altered columns) and applies them to your database in versioned steps.
- **psycopg2 / psycopg2-binary** → PostgreSQL database driver.  
  - `psycopg2` is the standard package.  
  - `psycopg2-binary` bundles precompiled binaries (easier install, but less flexible for production). You usually pick one, not both.

---

## ⚙️ Configuration & Environment
- **python-dotenv** → Loads environment variables from a `.env` file (e.g., database URL, secret keys) so you don’t hardcode sensitive values.

---

## 🔒 Security & Authentication
- **python-jose[cryptography]** → Handles JWT (JSON Web Tokens) and other cryptographic operations. Used for signing/verifying tokens in authentication flows.
- **passlib[bcrypt]** → Password hashing library. `bcrypt` is a secure algorithm for storing user passwords.

---

## 🧪 Testing & HTTP Clients
- **pytest** → Testing framework. Lets you write unit/integration tests for your FastAPI endpoints and backend logic.
- **httpx** → Async HTTP client. Useful for testing your API endpoints or making external API calls from your backend.

---

## 📐 Data Validation
- **pydantic** → Core of FastAPI’s request/response validation. You define schemas (`BaseModel` classes) and FastAPI automatically validates incoming JSON against them.

---

## 🧩 How They Work Together
Here’s the flow in your project:
1. **FastAPI** defines endpoints → served by **uvicorn**.
2. Requests are validated with **pydantic** models.
3. Auth handled with **python-jose** (JWT) + **passlib** (password hashing).
4. Data stored/retrieved via **SQLAlchemy** → migrations tracked by **Alembic** → DB driver is **psycopg2**.
5. Configs loaded with **python-dotenv**.
6. Tests written in **pytest**, often using **httpx** to simulate API calls.

---
