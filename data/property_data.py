import time
import os
import random

random_int = random.randint(1,6)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_IMAGE_PATH = os.path.join(BASE_DIR, 'images', f'House_{random_int}.png')

PROPERTY_DATA = [
  {
    "address": "a",
    "title": f"random property {int(time.time())}",
    "area": 1248,
    "rent_per_month": 12115,
    "file_path": TEST_IMAGE_PATH
  }
]