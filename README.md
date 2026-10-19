# 🚀 CacheBoost API

A high-performance backend API demonstrating the **Cache-Aside Pattern** using **FastAPI**, **Redis**, and **MongoDB**.

This project was built to understand how caching drastically reduces database load and improves API response times by serving frequently requested data directly from memory.

---

## 🏗️ Architecture Flow

```
Client ──► FastAPI (Uvicorn) ──► Redis ──┬── HIT  ──► 200 OK (instant, from memory)
                                         │
                                         └── MISS ──► MongoDB ──► save snapshot to Redis (TTL)
```

1. **Client** sends a request to `GET /products/{product_id}`.
2. **FastAPI (Uvicorn)** receives the request and checks Redis.
3. **Cache HIT:** If the data exists in Redis, it is returned instantly (MongoDB is untouched).
4. **Cache MISS:** If not in Redis, FastAPI queries MongoDB, fetches the data, and saves a "snapshot" back to Redis for future requests.

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Backend** | Python, FastAPI, Uvicorn |
| **Database** | MongoDB (PyMongo) |
| **Cache** | Redis (redis-py) |
| **Deployment / Tools** | Docker, Git |

---

## ⚙️ How to Run Locally

### 1. Prerequisites

Make sure you have **Docker** and **Python** installed on your system.

### 2. Start the Databases (Docker)

Run the MongoDB and Redis containers. Open your terminal and execute:

```bash
# Start Redis
docker run -d --name redis-cacheboost -p 6379:6379 redis:latest

# Start MongoDB (if not already running)
docker run -d --name mongo-cacheboost -p 27017:27017 mongo:latest
```

### 3. Set Up the Python Environment

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/akashhanc031-dotcom/CacheBoost.git
cd CacheBoost
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn pymongo redis
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

> **Note:** You will be prompted to enter your MongoDB password in the terminal when the app starts.
> Alternatively, set it beforehand using the `MONGO_PASSWORD` environment variable to skip the prompt.

---

## 🧪 Testing the Cache (Hit vs Miss)

1. Open your terminal to see the logs.
2. Request a product for the first time: `http://localhost:8000/products/P101`
   - Terminal output: `🐢 CACHE MISS: Querying MongoDB for P101`
3. Refresh the page or request the same URL again.
   - Terminal output: `⚡ CACHE HIT: Returning P101 from Redis`

---

## 🧠 Key Learnings & Scenarios

- **Speed:** Caching significantly reduces response time by skipping the database query.
- **Stale Data:** If a product is deleted from MongoDB but remains in Redis (until the TTL expires), the API will still return `200 OK`. This highlights the importance of **Cache Invalidation**.
- **TTL (Time-to-Live):** Redis keys are set to expire (e.g., 1 hour) to prevent old data from living in memory forever.

---

## 🔭 What's Next

- Benchmark the latency difference between cache hits and misses
- Implement robust cache invalidation strategies (e.g., delete-on-write)

---

## 📌 Author

**Akash** | BDA Student at CDAC Bangalore

- [LinkedIn](https://www.linkedin.com/in/akash-hanchate)
- [GitHub](https://github.com/akashhanc031-dotcom)
