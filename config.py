from dotenv import load_dotenv
import os

load_dotenv()

LANDLORD_EMAIL = os.getenv('LANDLORD_EMAIL')
LANDLORD_PASSWORD = os.getenv('LANDLORD_PASSWORD')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
TENANT_EMAIL = os.getenv('TENANT_EMAIL')