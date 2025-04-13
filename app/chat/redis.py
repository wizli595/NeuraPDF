import os
import redis
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the Redis URI safely
redis_uri = os.environ.get("REDIS_URI", "redis://localhost:6379")

print("Connecting to Redis using:", repr(redis_uri))

client = redis.Redis.from_url(
    redis_uri,
    decode_responses=True,
)