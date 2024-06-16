import time
import logging

logging.basicConfig(level=logging.INFO,format="%(lasctime)s - %(levelname)s -%(message)s")

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        elapsed_time=end_time - start_time
        logging.info (f"{func._name_}{elapsed_time:.4f}second")
        return result
    return wrapper


def logit(func):
    
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")  
        result = func(*args, **kwargs)  
        logging.info(f"Completado {func.__name__}")  
        return result  
    return wrapper