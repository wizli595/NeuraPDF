# 📚 NeuraPDF Project Overview

**NeuraPDF** is a full-stack application that allows users to upload and embed PDFs, then chat with them using AI-powered natural language queries. It integrates Flask (backend) and Svelte (frontend), with Redis and Celery for asynchronous task processing.

---

## 🧠 Project Structure and Folder Descriptions

### `app/`

Flask backend application.

- **`celery/`**: Celery integration with Flask. Includes:

  - `__init__.py`: Initializes Celery with Flask context.
  - `worker.py`: Entry point to launch the Celery worker process.

- **`chat/`**: Core logic for PDF chat functionality.

  - `chat.py`: Handles query-to-response logic.
  - `create_embeddings.py`: Generates vector embeddings for PDF content.
  - `score.py`: Scores responses based on relevance.
  - `models/`: Placeholder for chat-related data models.

- **`web/`**: Flask web layer and APIs.
  - `api.py`: Defines main Flask API routes.
  - `config/`: Configuration initialization.
  - `db/`: SQLAlchemy models for:
    - `conversation.py`, `message.py`, `pdf.py`, `user.py`: Represents app data.
  - `files.py`: PDF file processing utilities.
  - `hooks.py`: App startup/shutdown hooks.
  - `tasks/`: Celery background jobs (e.g. embedding generation).
  - `views/`: Flask route handlers for user-facing endpoints.

---

### `client/`

Frontend written in Svelte.

- **`src/api/axios.ts`**: Axios client config for API calls.
- **`components/`**: Reusable UI components like chat interface, navbar, forms.
- **`routes/`**: SvelteKit routing.
  - `(app)/auth/`: Auth pages (`signin`, `signup`, `signout`).
  - `(app)/chat/`: Main chat interface.
  - `(app)/documents/`: Upload and view documents.
  - `(app)/scores/`: View scoring results.
- **`store/`**: Svelte stores for reactive state management (auth, chat, errors, etc.).
- **`static/`**: Static assets like `favicon`, animation gif, and OpenAPI docs.
- Svelte + Tailwind + TypeScript configuration files.

---

### `instance/sqlite.db`

SQLite database file (auto-created for local development).

---

### 🧪 Other Files

- `Pipfile` / `requirements.txt`: Python dependencies.
- `tasks.py`: Entry point or glue code for CLI or debugging utilities.
- `README.md`: Project documentation.

---

## ⚙️ Technologies Used

- **Backend**: Flask, Celery, SQLAlchemy, Redis
- **Frontend**: SvelteKit, Tailwind CSS, TypeScript
- **AI / NLP**: Embedding models for vector search
- **Database**: SQLite (dev), pluggable for production

---

## 🛠 Install dependencies and set up the environment

```bash
pipenv install
pipenv shell
flask --app app.web init-db
```

---

# 🚀 Running the App

> The app requires **three separate processes**:
>
> 1. Python server
> 2. Celery worker
> 3. Redis server

---

## ✅ Start the Python Server

```bash
pipenv shell
inv dev
```

---

## ✅ Start the Celery Worker

```bash
pipenv shell
inv devworker
```

---

## ✅ Start Redis

```bash
redis-server
```

---

## 🔄 Reset the Database

```bash
pipenv shell
flask --app app.web init-db
```

---

## 💬 Summary

NeuraPDF enables users to upload PDFs, generate embeddings, and interact with them through a chat interface. It processes heavy embedding tasks asynchronously with Celery and Redis and provides a polished UI using SvelteKit.
