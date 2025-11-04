import logging
import jwt
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def generate_token(payload, secret_key, expires_in=3600):
    payload['exp'] = datetime.utcnow() + timedelta(seconds=expires_in)
    try:
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token
    except jwt.ExpiredSignatureError:
        logger.error("Token has expired")
        return None
    except jwt.InvalidTokenError:
        logger.error("Invalid token")
        return None

def verify_token(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        logger.error("Token has expired")
        return None
    except jwt.InvalidTokenError:
        logger.error("Invalid token")
        return None

def get_token_expiration(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload['exp']
    except jwt.ExpiredSignatureError:
        logger.error("Token has expired")
        return None
    except jwt.InvalidTokenError:
        logger.error("Invalid token")
        return None