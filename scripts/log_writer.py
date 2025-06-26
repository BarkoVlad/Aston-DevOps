#!/usr/bin/env python3
import os
import random
import string
import time
from datetime import datetime


def generate_random_string(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(random.randint(1, length)))


def main():
    app_dir = '/opt/app'
    os.makedirs(app_dir, exist_ok=True)
    log_file = os.path.join(app_dir, 'log.txt')
    
    while True:
        try:
            random_str = generate_random_string()
            log_entry = f"{datetime.now().isoformat()} - {random_str}\n"
            print(log_entry.strip())
            
            with open(log_file, 'a') as f:
                f.write(log_entry)
            
            time.sleep(17)
            
        except Exception as e:
            print(f": {e}")
            time.sleep(60)


if __name__ == '__main__':
    main()
