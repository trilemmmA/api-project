from datetime import datetime
from functools import wraps
import time

def log(message, level="INFO"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("operations.log", "a", encoding='utf-8') as f:
        f.write(f"[{current_time}] [{level}] {message}\n")
        
def call_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        
        main_func = func(*args, **kwargs)
        
        end = time.time()
        log(f"'{func.__name__}' is called | completed in {end - start:.4f} seconds")
        
        return main_func
    return wrapper

