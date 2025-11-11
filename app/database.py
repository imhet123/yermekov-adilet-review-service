import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from asyncio import TimeoutError as AsyncTimeoutError

# Загружаем переменные окружения (для локального тестирования, Render игнорирует)
load_dotenv() 

# 1. Получаем строку подключения из переменной окружения
MONGO_URI = os.getenv("MONGO_URI", "mongodb://review-mongo:27017")

# 2. Получаем имя базы данных.
DB_NAME = os.getenv("DB_NAME", "reviewdb")

# Инициализация клиента
client = None
db = None

# Дополнительный тест для проверки, что MONGO_URI был установлен.
if MONGO_URI == "mongodb://review-mongo:27017":
    print("WARNING: Using local database URI. Ensure MONGO_URI is set in production!")


async def connect_to_mongo():
    """Подключается к MongoDB Atlas при старте приложения."""
    global client, db
    
    try:
        # Устанавливаем таймаут на 5 секунд для проверки соединения
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        
        # Попытка выполнить простую команду 'ping' для проверки соединения
        await client.admin.command('ping') 
        
        db = client[DB_NAME]
        print("✅ MongoDB connection successful.")
        
    except AsyncTimeoutError:
        # Специальная обработка для таймаута
        print("=========================================================================================")
        print("🛑🛑🛑 ERROR: MONGODB CONNECTION TIMEOUT 🛑🛑🛑")
        print("Possible causes: MONGO_URI is incorrect or Render's IP is not whitelisted on MongoDB Atlas.")
        print("=========================================================================================")
        raise ConnectionError("MongoDB connection timed out.")
        
    except Exception as e:
        # Обработка любых других ошибок подключения
        print("=========================================================================================")
        print("🛑🛑🛑 ERROR: FAILED TO CONNECT TO MONGODB ATLAS 🛑🛑🛑")
        print(f"Details: {e.__class__.__name__}: {e}")
        print("Check your MONGO_URI and network access settings on Atlas.")
        print("=========================================================================================")
        
        # Важно: мы перевызываем ошибку, чтобы Render корректно зафиксировал сбой старта
        raise e


async def close_mongo_connection():
    """Закрывает соединение при выключении приложения."""
    global client
    if client:
        client.close()
        print("MongoDB connection closed.")


def get_mongo_client() -> AsyncIOMotorClient:
    return client


def get_database():
    return db
