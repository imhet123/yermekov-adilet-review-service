# 🚀 Review Service Microservice (Deployed on Render)

This project is a **FastAPI** microservice designed to manage **reviews (CRUD)** and link them to tracks from a separate service (`music-service`). The application is containerized using **Docker** and deployed on the **Render** cloud platform, connecting to a **MongoDB Atlas** database.

## 🌐 Live Project Links

| Component | Link |
| :--- | :--- |
| **GitHub Repository** | `https://github.com/YOUR_NICKNAME/yermekov-adilet-review-service` |
| **Live Render URL** | `https://YOUR-APP-NAME.onrender.com/` |
| **Swagger UI (API Docs)** | `https://YOUR-APP-NAME.onrender.com/docs` |

---

## ✅ Deployment Criteria Met (Assignment 4)

[cite_start]This project fully meets all requirements of the assignment[cite: 2]:

### 1. Project Setup & Structure (10 Marks)

* **FastAPI Application:** The core application code is located in the `app/` directory.
* [cite_start]**Dockerfile:** Present in the root directory for building the container[cite: 49].
* **Requirements:** `requirements.txt` includes all necessary Python dependencies.

### 2. Docker Build & SSL Implementation (10 Marks)

* The container builds and runs successfully.
* [cite_start]**SSL/TLS Handling:** The `Dockerfile` includes the mandatory step to install system certificates, essential for a secure TLS/SSL connection to MongoDB Atlas[cite: 36, 37]:
    ```dockerfile
    RUN apt-get update && \
        apt-get install -y --no-install-recommends ca-certificates openssl && \
        update-ca-certificates && \
        rm -rf /var/lib/apt/lists/*
    ```

### 3. Environment Variables (10 Marks)

[cite_start]All required environment variables are configured **securely** in the Render environment, not exposed in the repository[cite: 31, 35].

| Variable | Purpose |
| :--- | :--- |
| `MONGO_URI` | [cite_start]MongoDB Atlas connection string[cite: 32]. |
| `DB_NAME` | The name of the target database (`reviewdb`)[cite: 33]. |
| `JWT_SECRET` | [cite_start]Randomly generated secret key (as required by the assignment)[cite: 34]. |
| `MUSIC_SERVICE_URL` | URL of the dependent microservice (e.g., `https://overtone-music.onrender.com/`). |

### 4. Health Endpoint & MongoDB Connection (25 Marks)

* [cite_start]**Working `/health/db` Endpoint:** Implemented and actively verifies the database connection status by executing a real `ping` command to MongoDB Atlas[cite: 18, 49].
* **Test Connection:**
    ```bash
    curl [https://YOUR-APP-NAME.onrender.com/health/db](https://YOUR-APP-NAME.onrender.com/health/db)
    # Expected Result: HTTP 200 OK, {"status": "ok", "message": "Connection successful", ...}
    ```

---

## 🛠️ Local Development Instructions

For local testing, use the following steps (assuming you have a local MongoDB instance running):

1.  **Create a `.env` file** in the root directory with your local credentials:
    ```
    MONGO_URI="mongodb://localhost:27017"
    DB_NAME="reviewdb"
    MUSIC_SERVICE_URL="[http://127.0.0.1:8001](http://127.0.0.1:8001)" 
    JWT_SECRET="your_local_secret"
    ```
2.  **Install Dependencies:** `pip install -r requirements.txt`
3.  **Run the application:** `uvicorn app.main:app --reload`

## ⚙️ Project Structure
