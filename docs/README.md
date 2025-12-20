To run your FastAPI app with **Uvicorn** (the ASGI server most commonly used with FastAPI), the command looks like this:

```bash
uvicorn app.main:app --reload
```

### 🔹 Breakdown of the command
- `uvicorn` → the server executable  
- `app.main:app` →  
  - `app` = your **package/folder name**  
  - `main` = the **Python file** (`main.py`) inside that folder  
  - `app` = the **FastAPI instance** created in `main.py` (`app = FastAPI()`)  
- `--reload` → enables auto‑reload when you change code (great for development)

---

### 🔹 Variations
- If your `main.py` is at the **root level** (not inside `app/`), run:
  ```bash
  uvicorn main:app --reload
  ```
- To specify host and port:
  ```bash
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```

---

👉 Always use `--reload` in dev, but **never in production**. In production, you’d run something like:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

or wrap it with a process manager like **Gunicorn** or **Docker** for robustness.

---