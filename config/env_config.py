import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv

# ##### PATH CONFIGURATION ################################

# fetch FastAPI's project directory
BASE_DIR = dirname(dirname(abspath(__file__)))

dotenv_path = join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# ##### DATABASE CONFIGURATION ###############################
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABSE_PASSWORD")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
RESET_PWD_LINK_URL = os.environ.get("RESET_PWD_LINK_URL")
