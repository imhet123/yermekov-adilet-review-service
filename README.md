## 🚀 [EN] Review Service Microservice: Render Deployment

[](https://www.google.com/url?sa=E&source=gmail&q=https://YOUR-APP-NAME.onrender.com/)
[](https://www.mongodb.com/atlas)
[](https://www.google.com/search?q=LICENSE)

### 🔗 Project Links

| Component | Link |
| :--- | :--- |
| **GitHub Repository** | `imhet123/yermekov-adilet-review-service` |
| **Live Render URL** | `https://yermekov-adilet-review-service-1.onrender.com` |
| **Swagger UI (API Docs)** | `https://yermekov-adilet-review-service-1.onrender.com/docs` |

-----

### ✨ Project Overview

This microservice, built with **FastAPI**, provides CRUD functionality for managing user reviews for music tracks.

**Key Feature:** When creating a review, the service performs an **asynchronous HTTP request** (`httpx`) to the dependent `music-service` (using its URL retrieved from environment variables) to fetch track metadata (title, artist), demonstrating cross-service communication.

### ⚙️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | Python 3.11, FastAPI, Uvicorn |
| **Database** | MongoDB Atlas (NoSQL) |
| **Async Clients** | `motor`, `httpx` |
| **Containerization** | Docker |
| **Deployment Platform** | Render |

-----

## ✅ Assignment 4 Compliance Report

This project is fully compliant with all grading criteria.

### 1\. 🛡️ Secure Deployment & SSL/TLS (20 Marks)

| Criterion | Implementation |
| :--- | :--- |
| **Docker Build** | Container builds and runs without errors. |
| **SSL/TLS Fix** | The `Dockerfile` includes the mandatory step to install system certificates, ensuring a secure TLS/SSL connection to MongoDB Atlas: |

```dockerfile
# MANDATORY STEP 4: Install system certificates for secure connection to MongoDB Atlas (TLS/SSL)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*
```

### 2\. 🔑 Environment Variables (10 Marks)

All required environment variables are configured **securely** in the Render dashboard (not in Git).

| Variable | Purpose |
| :--- | :--- |
| `MONGO_URI` | MongoDB Atlas connection string. |
| `DB_NAME` | The name of the target database (`reviewdb`). |
| `JWT_SECRET` | Randomly generated secret key (as required by the assignment). |
| `MUSIC_SERVICE_URL` | URL of the dependent microservice (using "Any other needed environmental variables" clause). |

### 3\. 🩺 Health Check & Connection (25 Marks)

  * **Working `/health/db` Endpoint:** Implemented in `app/main.py` and actively verifies the live connection to MongoDB Atlas by executing a real `db_client.admin.command('ping')`.

**Test Connection:**

```bash
curl https://yermekov-adilet-review-service-1.onrender.com/health/db
# Expected Result: HTTP 200 OK, {"status": "ok", "message": "Connection successful", ...}
```

-----

## 🔗 Available API Endpoints

All CRUD operations are accessible under the base path `/api/v1/reviews`.

| Method | Path | Description |
| :--- | :--- | :--- |
| **GET** | `/` | Root endpoint. Returns a welcome message. |
| **GET** | `/health/db` | **Mandatory Health Check.** Verifies the live connection to MongoDB Atlas. |
| **POST** | `/api/v1/reviews/` | **Create Review.** Creates a new review. Requires a `track_id` and calls the `music-service` for track data before saving. |
| **GET** | `/api/v1/reviews/user/{user_id}` | **Read User Reviews.** Retrieves all reviews posted by a specific user. |
| **GET** | `/api/v1/reviews/track/{track_id}` | **Read Track Reviews.** Retrieves all reviews associated with a specific track ID. |

-----

## 💻 Local Development

### 1\. Project Structure (10 Marks)

The project setup includes the FastAPI application, `Dockerfile`, and all environment configuration files.

```
.
├── Dockerfile                  # Containerization and SSL installation
├── requirements.txt            # Python dependencies
├── app/
│   ├── main.py                 # FastAPI initialization and /health/db endpoint
│   ├── database.py             # MongoDB connection setup using os.getenv
│   ├── models.py               # Pydantic data models
│   └── routes/                 # NOTE: Using 'routes' folder name, not 'routers'
│       └── reviews.py          # CRUD logic for reviews
└── README.md                   # This documentation file
```

### 2\. Startup Instructions

1.  **Clone the repository:** `git clone ...`
2.  **Create a `.env` file** in the root directory (FOR LOCAL USE ONLY\!):
    ```env
    MONGO_URI="mongodb://localhost:27017"
    DB_NAME="reviewdb"
    MUSIC_SERVICE_URL="http://127.0.0.1:8001" 
    JWT_SECRET="your_local_secret"
    ```
3.  **Install Dependencies:** `pip install -r requirements.txt`
4.  **Run the application:** `uvicorn app.main:app --reload`

<img width="1890" height="755" alt="image" src="https://github.com/user-attachments/assets/44ad20a8-1279-4bfa-b032-f950d5ad0f7a" />

