import os
import redis

#=============================================================
# Configura Flask-Caching per redis
# app.config["CACHE_TYPE"] = "RedisCache"
# app.config["CACHE_REDIS_URL"] = os.getenv("REDIS_URL")

# Inizializza il client Redis senza Flask-Caching
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True,
    socket_timeout=5,
    socket_connect_timeout=5,
    retry_on_timeout=True
)

#=============================================================