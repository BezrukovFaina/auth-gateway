import logging
import hashlib
import hmac
import json
import os
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_hmac_signature(data: Dict, secret_key: str) -> str:
    # Calculate HMAC signature for authentication
    return hmac.new(secret_key.encode(), json.dumps(data).encode(), hashlib.sha256).hexdigest()

def load_config(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse config file: {e}")
        return {}

def validate_config(config: Dict) -> bool:
    required_keys = ['client_id', 'client_secret', 'api_url']
    return all(key in config for key in required_keys)

def get_environment_variable(var_name: str) -> str:
    return os.environ.get(var_name)

def split_list(input_list: List, chunk_size: int) -> List[List]:
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]