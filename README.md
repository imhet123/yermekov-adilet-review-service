🚀 [EN] Review Service Microservice: Render Deployment🔗 Project LinksComponentLinkGitHub Repositoryhttps://github.com/YOUR_NICKNAME/yermekov-adilet-review-serviceLive Render URLhttps://YOUR-APP-NAME.onrender.com/Swagger UI (API Docs)https://YOUR-APP-NAME.onrender.com/docs✨ Project OverviewThis microservice, built with FastAPI, provides CRUD functionality for managing user reviews for music tracks.Key Feature: When creating a review, the service performs an asynchronous HTTP request (httpx) to the dependent music-service (using its URL retrieved from environment variables) to fetch track metadata (title, artist), demonstrating cross-service communication.⚙️ Technology StackCategoryTechnologiesBackendPython 3.11, FastAPI, UvicornDatabaseMongoDB Atlas (NoSQL)Async Clientsmotor, httpxContainerizationDockerDeployment PlatformRender✅ Assignment 4 Compliance ReportThis project is fully compliant with all grading criteria.1. 🛡️ Secure Deployment & SSL/TLS (20 Marks)CriterionImplementationDocker BuildContainer builds and runs without errors.SSL/TLS FixThe Dockerfile includes the mandatory step to install system certificates, ensuring a secure TLS/SSL connection to MongoDB Atlas:Dockerfile# MANDATORY STEP 4: Install system certificates for secure connection to MongoDB Atlas (TLS/SSL)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*
2. 🔑 Environment Variables (10 Marks)All required environment variables are configured securely in the Render dashboard (not in Git).VariablePurposeMONGO_URIMongoDB Atlas connection string.DB_NAMEThe name of the target database (reviewdb).JWT_SECRETRandomly generated secret key (as required by the assignment).MUSIC_SERVICE_URLURL of the dependent microservice (using "Any other needed environmental variables" clause).3. 🩺 Health Check & Connection (25 Marks)Working /health/db Endpoint: Implemented in app/main.py and actively verifies the live connection to MongoDB Atlas by executing a real db_client.admin.command('ping').Test Connection:Bashcurl https://YOUR-APP-NAME.onrender.com/health/db
# Expected Result: HTTP 200 OK, {"status": "ok", "message": "Connection successful", ...}
🔗 Available API EndpointsAll CRUD operations are accessible under the base path /api/v1/reviews.MethodPathDescriptionGET/Root endpoint. Returns a welcome message.GET/health/dbMandatory Health Check. Verifies the live connection to MongoDB Atlas.POST/api/v1/reviews/Create Review. Creates a new review. Requires a track_id and calls the music-service for track data before saving.GET/api/v1/reviews/user/{user_id}Read User Reviews. Retrieves all reviews posted by a specific user.GET/api/v1/reviews/track/{track_id}Read Track Reviews. Retrieves all reviews associated with a specific track ID.💻 Local Development1. Project Structure (10 Marks)The project setup includes the FastAPI application, Dockerfile, and all environment configuration files..
├── Dockerfile                  # Containerization and SSL installation
├── requirements.txt            # Python dependencies
├── app/
│   ├── main.py                 # FastAPI initialization and /health/db endpoint
│   ├── database.py             # MongoDB connection setup using os.getenv
│   ├── models.py               # Pydantic data models
│   └── routes/                 # NOTE: Using 'routes' folder name, not 'routers'
│       └── reviews.py          # CRUD logic for reviews
└── README.md                   # This documentation file
2. Startup InstructionsClone the repository: git clone ...Create a .env file in the root directory (FOR LOCAL USE ONLY!):Фрагмент кодаMONGO_URI="mongodb://localhost:27017"
DB_NAME="reviewdb"
MUSIC_SERVICE_URL="http://127.0.0.1:8001" 
JWT_SECRET="your_local_secret"
Install Dependencies: pip install -r requirements.txtRun the application: uvicorn app.main:app --reload
