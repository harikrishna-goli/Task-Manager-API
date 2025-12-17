## ✅ Basic Requirements for the Task Manager API

### Functional Requirements
- **User Authentication**
  - Register new users.
  - Login with credentials.
  - Issue JWT tokens for secure, stateless authentication.

- **Task Management**
  - Create, Read, Update, Delete (CRUD) tasks.
  - Each task has: `title`, `description`, `deadline`, `status`.
  - Status values: `todo`, `in_progress`, `done`.

- **Filtering & Search**
  - Query tasks by status.
  - Filter tasks due today.
  - Keyword search in title/description.

### Non-Functional Requirements
- **Database Schema Evolution**
  - Alembic migrations for reproducible schema setup.

- **Containerization**
  - Multi-container setup (API + DB) using Docker Compose.

- **Testing**
  - Pytest suite with isolated test database.
  - Automated test execution in CI/CD pipeline.

- **CI/CD**
  - GitHub Actions pipeline.
  - Run tests and migrations automatically on push/PR.
