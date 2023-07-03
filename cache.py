import redis
from dotenv.main import load_dotenv
import os


load_dotenv()


# redis for debug
if os.environ.get("DEBUG"):
    _cache = redis.Redis(host='localhost', port=6379, decode_responses=True)
else:
    # redis for production
    _cache = redis.Redis(
        host=os.environ.get('REDIS_HOST'),
        port=os.environ.get("REDIS_PORT"),
        # use your Redis user. More info https://redis.io/docs/management/security/acl/
        username=os.environ.get('REDIS_USERNAME'),
        password=os.environ.get("REDIS_PASSWORD"),  # use your Redis password
        ssl=os.environ.get('REDIS_SSL'),
        ssl_certfile="./redis_user.crt",
        ssl_keyfile="./redis_user_private.key",
        ssl_ca_certs="./redis_ca.pem",
    )


