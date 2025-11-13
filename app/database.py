import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv() 

# Значение по умолчанию для локального запуска
MONGO_URI = os.getenv("MONGO_URI", "mongodb://review-mongo:27017") 

# Имя БД по умолчанию
DB_NAME = os.getenv("DB_NAME", "reviewdb") 

# Инициализация клиента (Происходит при загрузке модуля)
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

if MONGO_URI == "mongodb://review-mongo:27017": 
    print("WARNING: Using local database URI. Ensure MONGO_URI is set in production!")


async def connect_to_mongo():
    """Подключение к БД при старте."""
    # Соединение уже создано выше, здесь просто печатаем сообщение.
    # Проверка соединения выполняется в /health/db.
    print("Connecting to MongoDB...")

async def close_mongo_connection():
    """Отключение от БД при остановке."""
    global client
    if client:
        client.close()
    print("Closing MongoDB connection...")

def get_mongo_client() -> AsyncIOMotorClient:
    return client

def get_database() -> AsyncIOMotorClient:
    return db
