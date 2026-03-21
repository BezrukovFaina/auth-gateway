import logging
import jwt
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def generate_token(payload, secret_key, expires_in=3600):
    """Generates a JWT token with the given payload and expiration time."""
    payload['exp'] = datetime.utcnow() + timedelta(seconds=expires_in)
    try:
        return jwt.encode(payload, secret_key, algorithm='HS256')
    except Exception as e:
        logger.error(f"Error generating token: {str(e)}")
        return None

def verify_token(token, secret_key):
    """Verifies a JWT token and returns the payload if valid."""
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError as e:
        logger.error("Token has expired")
        return None
    except jwt.InvalidTokenError as e:
        logger.error(f"Invalid token: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Error verifying token: {str(e)}")
        return None

def get_token_expiration(token, secret_key):
    """Gets the expiration time of a JWT token."""
    try:
        payload = verify_token(token, secret_key)
        if payload:
            return payload['exp']
    except Exception:
        pass
    return None