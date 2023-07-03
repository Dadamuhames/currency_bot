import redis
from dotenv.main import load_dotenv
import os


load_dotenv()


# redis for debug
if os.environ.get("DEBUG") == 'True':
    _cache = redis.Redis(host='localhost', port=6379, decode_responses=True)
else:
    # redis for production
    _cache = redis.Redis(
        host=os.environ.get('REDIS_HOST'),
        port=os.environ.get("REDIS_PORT"),
        password=os.environ.get("REDIS_PASSWORD"),
        ssl=True
    )


