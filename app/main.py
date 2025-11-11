import os
from fastapi import FastAPI, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient

# Импорт функций для управления БД
from .db import connect_to_mongo, close_mongo_connection, get_mongo_client, get_database

# ИЗМЕНЕНО: Импортируем ваш роутер для отзывов (предполагаю, что он называется reviews)
from .routers import reviews 

# ИЗМЕНЕНО: Инициализация FastAPI приложения
app = FastAPI(
    title="Review Service Microservice", # <-- ИЗМЕНЕНО
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# === Жизненный цикл приложения (Без изменений) ===

@app.on_event("startup")
async def startup_db_client():
    """Подключение к БД при старте."""
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    """Отключение от БД при остановке."""
    await close_mongo_connection()

# === Health Check Endpoint (Без изменений, он идеален) ===

@app.get("/health/db", tags=["Health"], summary="Check connection to MongoDB Atlas")
async def check_db_health(db_client: AsyncIOMotorClient = Depends(get_mongo_client)):
    """
    Проверяет, активно ли соединение с MongoDB Atlas, выполняя простую команду.
    """
    if db_client is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="MongoDB Client is not initialized"
        )
        
    try:
        ping_result = await db_client.admin.command('ping')
        
        if ping_result.get('ok') == 1:
            return {
                "status": "ok",
                "database": "MongoDB Atlas",
                "message": "Connection successful",
                "ping_result": ping_result
            }
        else:
            raise Exception("Ping command did not return status 'ok'")

    except Exception as e:
        print(f"Health check failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database connection failed: {e.__class__.__name__}"
        )

# === ИЗМЕНЕНО: Подключаем CRUD роуты для "Reviews" ===

app.include_router(reviews.router, prefix="/api/v1/reviews", tags=["Reviews"]) # <-- ИЗМЕНЕНО

@app.get("/", tags=["Root"])
async def read_root():
    """Базовый эндпоинт для проверки работы FastAPI."""
    # ИЗМЕНЕНО:
    return {"message": "Welcome to the Review Service API. Check /docs for endpoints."}