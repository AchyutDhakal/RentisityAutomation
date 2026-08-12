import time
import os
import random

random_int = random.randint(1,6)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_IMAGE_PATH = os.path.join(BASE_DIR, 'images', f'House_{random_int}.png')
random_number = random.randint(100, 9999999)

PROPERTY_DATA = [
  {
    "address": "a",
    "title": f"single_tenant 0{random_number}",
    "area": random_number,
    "rent_per_month": random_number,
    "file_path": TEST_IMAGE_PATH,
    "property_type": "single",
    "group_creator": None,
    "payment_responsibility": None,
    "contract": None
  },
  {
    "address": "a",
    "title": f"multiple_tenant, group_creator_tenant, payment_responsibility_lead, contract_lead_tenant 1{random_number}",
    "area": random_number,
    "rent_per_month": random_number,
    "file_path": TEST_IMAGE_PATH,
    "property_type": "multiple",
    "group_creator": "tenant",
    "payment_responsibility": "lead",
    "contract": "lead_tenant"
  },
  {
    "address": "a",
    "title": f"multiple_tenant, group_creator_tenant, payment_responsibility_lead, contract_everyone 2{random_number}",
    "area": random_number,
    "rent_per_month": random_number,
    "file_path": TEST_IMAGE_PATH,
    "property_type": "multiple",
    "group_creator": "tenant",
    "payment_responsibility": "lead",
    "contract": "everyone"
  },
  {
      "address": "a",
      "title": f"multiple_tenant, group_creator_tenant, payment_responsibility_individual 3{random_number}",
      "area": random_number,
      "rent_per_month": random_number,
      "file_path": TEST_IMAGE_PATH,
      "property_type": "multiple",
      "group_creator": "tenant",
      "payment_responsibility": "individual",
      "contract": None
  },
  {
      "address": "a",
      "title": f"multiple_tenant, group_creator_landlord, payment_responsibility_lead 4{random_number}",
      "area": random_number,
      "rent_per_month": random_number,
      "file_path": TEST_IMAGE_PATH,
      "property_type": "multiple",
      "group_creator": "landlord",
      "payment_responsibility": "lead",
      "contract": None
  },
  {
      "address": "a",
      "title": f"multiple_tenant, group_creator_tenant, payment_responsibility_individual 5{random_number}",
      "area": random_number,
      "rent_per_month": random_number,
      "file_path": TEST_IMAGE_PATH,
      "property_type": "multiple",
      "group_creator": "landlord",
      "payment_responsibility": "individual",
      "contract": None
  },
]