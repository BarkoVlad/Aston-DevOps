#!/usr/bin/env python3
import os
import random
import string
import time
from datetime import datetime

def generate_random_string(length=20):
    """     20 """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(random.randint(1, length)))

def ensure_log_file(log_path):
    """  -   """
    log_dir = os.path.dirname(log_path)
    try:
        os.makedirs(log_dir, exist_ok=True)
        if not os.path.exists(log_path):
            with open(log_path, 'w') as f:
                f.write("")
        os.chmod(log_path, 0o644)
        os.chmod(log_dir, 0o755)
    except Exception as e:
        print(f"   -: {e}")
        raise

def main():
    app_dir = '/opt/app'
    log_file = os.path.join(app_dir, 'log.txt')
    
    #     
    ensure_log_file(log_file)
    
    while True:
        try:
            random_str = generate_random_string()
            log_entry = f"{datetime.now().isoformat()} - {random_str}\n"
            
            #    
            if not os.access(log_file, os.W_OK):
                ensure_log_file(log_file)
                
            with open(log_file, 'a') as f:
                f.write(log_entry)
                f.flush()  #    
                
            time.sleep(17)
            
        except PermissionError as pe:
            print(f"  : {pe}")
            time.sleep(60)
        except Exception as e:
            print(f" : {e}")
            time.sleep(30)

if __name__ == '__main__':
    main()