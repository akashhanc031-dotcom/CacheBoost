import json
from fastapi import FastAPI, HTTPException
from app.database import products_collection
from app.redis_client import redis_client  # <-- Import Redis

app = FastAPI(
    title="CacheBoost API",
    description="A caching performance demonstration using Redis and MongoDB",
    version="0.1.0",
)

@app.get("/")
def home():
    return {
        "project": "CacheBoost",
        "status": "running",
        "message": "Welcome to CacheBoost API!",
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/products/{product_id}")
def get_product(product_id: str):
    # 1. Cache Key banao
    cache_key = f"product:{product_id}"

    # 2. Check Redis
    cached_product = redis_client.get(cache_key)

    if cached_product:
        print(f"⚡ CACHE HIT: Returning {product_id} from Redis")
        return json.loads(cached_product) # String ko wapas Dict mein convert karo

    # 3. Cache Miss - MongoDB se laao
    print(f"🐢 CACHE MISS: Querying MongoDB for {product_id}")
    
    product = products_collection.find_one(
        {"product_id": product_id},
        {"_id": 0}
    )

    if product:
        # 4. MongoDB se aaya data Redis mein save karo (1 ghante ke liye)
        redis_client.setex(
            name=cache_key,
            time=3600, 
            value=json.dumps(product) # Dict ko String mein convert karke save karo
        )
        return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )