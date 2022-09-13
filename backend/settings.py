import os

from dotenv import load_dotenv

load_dotenv()


DB_USER = os.getenv("DB_USER")
DATABASE = os.getenv("DATABASE")
DB_PASSWORD = os.getenv("DB_PASSWORD")

TEST_DATABASE = os.getenv("TEST_DATABASE")
TEST_DB_USER = os.getenv("TEST_DB_USER")
TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")
