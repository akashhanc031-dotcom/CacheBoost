# 🚀 CacheBoost API

A high-performance backend API demonstrating the **Cache-Aside Pattern** using FastAPI, Redis, and MongoDB. 

This project was built to understand how caching drastically reduces database load and improves API response times by serving frequently requested data directly from memory.

## 🏗️ Architecture Flow

1. **Client** sends a request to `GET /products/{product_id}`.
2. **FastAPI (Uvicorn)** receives the request and checks **Redis**.
3. **Cache HIT:** If the data exists in Redis, it is returned instantly (MongoDB is untouched).
4. **Cache MISS:** If not in Redis, FastAPI queries **MongoDB**, fetches the data, and saves a "snapshot" back to Redis for future requests.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Database:** MongoDB (PyMongo)
* **Cache:** Redis (redis-py)
* **Deployment/Tools:** Docker, Git

## ⚙️ How to Run Locally

### 1. Prerequisites
Make sure you have Docker and Python installed on your system.

### 2. Start the Databases (Docker)
Run MongoDB and Redis containers:
```bash
# Start Redis
docker run -d --name redis-cacheboost -p 6379:6379 redis:latest

# Start MongoDB (if not already running)
docker run -d --name mongo-cacheboost -p 27017:27017 mongo:latest
