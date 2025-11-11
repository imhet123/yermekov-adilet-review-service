import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv() 

# ИЗМЕНЕНО: Значение по умолчанию для локального запуска (docker-compose)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://review-mongo:27017") # <-- ИЗМЕНЕНО

# ИЗМЕНЕНО: Имя БД по умолчанию (например, "reviewdb" или "reviews")
DB_NAME = os.getenv("DB_NAME", "reviewdb") # <-- ИЗМЕНЕНО

# Инициализация клиента (Без изменений)
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# ИЗМЕНЕНО: Обновлена проверка для локального запуска
if MONGO_URI == "mongodb://review-mongo:27017": # <-- ИЗМЕНЕНО
    print("WARNING: Using local database URI. Ensure MONGO_URI is set in production!")

# Функции get_database и get_mongo_client (предполагаю, они у вас есть)
# (Если их нет, скопируйте их из music-service)

async def connect_to_mongo():
    global client
    # (Ваш код подключения...)
    print("Connecting to MongoDB...")

async def close_mongo_connection():
    global client
    # (Ваш код отключения...)
    print("Closing MongoDB connection...")

def get_mongo_client() -> AsyncIOMotorClient:
    return client

def get_database() -> AsyncIOMotorClient:
    return db