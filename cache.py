# Description: This file contains functions to cache data to avoid unnecessary API calls.
import json
import os

CACHE_FILE = "cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    else:
        return {}

def save_cache(cache_data):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache_data, f, indent=4)

def update_cache(key, data):
    cache = load_cache()
    cache[key] = data
    save_cache(cache)

def get_cached_data(key):
    cache = load_cache()
    return cache.get(key, None)