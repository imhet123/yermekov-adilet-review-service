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

This project fully meets all requirements of the assignment:

### 1. Project Setup & Structure (10 Marks)

* **FastAPI Application:** The core application code is located in the `app/` directory.
* **Dockerfile:** Present in the root directory for building the container.
* **Requirements:** `requirements.txt` includes all necessary Python dependencies.

### 2. Docker Build & SSL Implementation (10 Marks)

* The container builds and runs successfully.
* **SSL/TLS Handling:** The `Dockerfile` includes the mandatory step to install system certificates, essential for a secure TLS/SSL connection to MongoDB Atlas:
    ```dockerfile
    RUN apt-get update && \
        apt-get install -y --no-install-recommends ca-certificates openssl && \
        update-ca-certificates && \
        rm -rf /var/lib/apt/lists/*
    ```

### 3. Environment Variables (10 Marks)

All required environment variables are configured **securely** in the Render environment, not exposed in the repository.

| Variable | Purpose |
| :--- | :--- |
| `MONGO_URI` | MongoDB Atlas connection string. |
| `DB_NAME` | The name of the target database (`reviewdb`). |
| `JWT_SECRET` | Randomly generated secret key (as required by the assignment). |
| `MUSIC_SERVICE_URL` | URL of the dependent microservice (e.g., `https://overtone-music.onrender.com/`). |

### 4. Health Endpoint & MongoDB Connection (25 Marks)

* **Working `/health/db` Endpoint:** Implemented and actively verifies the database connection status by executing a real `ping` command to MongoDB Atlas.
* **Test Connection:**
    ```bash
    curl [https://YOUR-APP-NAME.onrender.com/health/db](https://YOUR-APP-NAME.onrender.com/health/db)
    # Expected Result: HTTP 200 OK, {"status": "ok", "message": "Connection successful", ...}
    ```
---

## 🔗 Available Endpoints

The service provides the following endpoints under the base path `/api/v1/reviews` (for CRUD operations) and general health checks.

| Method | Path | Description |
| :--- | :--- | :--- |
| **GET** | `/` | Root endpoint. Returns a welcome message. |
| **GET** | `/health/db` | **Mandatory Health Check.** Verifies the live connection to MongoDB Atlas. |
| **POST** | `/api/v1/reviews/` | **Create Review.** Creates a new review. Requires a `track_id` and calls the `music-service` for track data before saving. |
| **GET** | `/api/v1/reviews/user/{user_id}` | **Read User Reviews.** Retrieves all reviews posted by a specific user. |
| **GET** | `/api/v1/reviews/track/{track_id}` | **Read Track Reviews.** Retrieves all reviews associated with a specific track ID. |

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
. ├── Dockerfile # Containerization and SSL installation ├── requirements.txt # Python dependencies ├── app/ │ ├── main.py # FastAPI initialization and /health/db endpoint │ ├── database.py # MongoDB connection setup using os.getenv │ ├── models.py # Pydantic data models │ └── routes/ │ └── reviews.py # CRUD logic for reviews └── README.md # This documentation file
<img width="1913" height="895" alt="image" src="https://github.com/user-attachments/assets/bb79418d-6595-47ab-af4c-779bda2b50ad" />


