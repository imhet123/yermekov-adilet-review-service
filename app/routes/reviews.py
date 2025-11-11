import os  # <-- 1. Добавьте этот импорт
from fastapi import APIRouter, HTTPException
from app.models import Review
from app.database import db
from bson import ObjectId
import httpx

router = APIRouter()
collection = db["reviews"]

# 2. Получаем URL из переменной окружения.
# Мы используем ваш URL как значение ПО УМОЛЧАНИЮ, на случай если переменная не задана.
MUSIC_SERVICE_URL = os.getenv("MUSIC_SERVICE_URL", "https://overtone-music.onrender.com/")

def fix_id(doc):
    """Преобразует ObjectId в строку, чтобы JSON не падал"""
    if not doc:
        return doc
    doc["_id"] = str(doc["_id"])
    return doc


@router.post("/")
async def create_review(review: Review):
    # Получаем данные о треке из music-service
    async with httpx.AsyncClient() as client:
        try:
            # Убедимся, что URL заканчивается на /
            base_url = MUSIC_SERVICE_URL.rstrip('/') + '/'
            resp = await client.get(f"{base_url}tracks/{review.track_id}") # <-- 3. Используем base_url
            
        except Exception as e:
            print(f"Error calling music-service: {e}") # Лучше логировать ошибку
            raise HTTPException(status_code=503, detail="Music-service unavailable")

        if resp.status_code != 200:
            raise HTTPException(status_code=404, detail="Track not found in music-service")

        track_data = resp.json()

    # Объединяем данные трека с рецензией
    review_data = review.dict()
    review_data["track_title"] = track_data.get("title")
    review_data["artist_name"] = track_data.get("artist_name", "Unknown Artist")
    review_data["album"] = track_data.get("album")
    review_data["year"] = track_data.get("year")

    # Сохраняем в MongoDB
    result = await collection.insert_one(review_data)
    created = await collection.find_one({"_id": result.inserted_id})
    return {"message": "Review created", "review": fix_id(created)}


@router.get("/user/{user_id}")
async def get_user_reviews(user_id: str):
    reviews = await collection.find({"user_id": user_id}).to_list(100)
    return [fix_id(r) for r in reviews]


@router.get("/track/{track_id}")
async def get_track_reviews(track_id: str):
    reviews = await collection.find({"track_id": track_id}).to_list(100)
    return [fix_id(r) for r in reviews]