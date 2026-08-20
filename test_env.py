from dotenv import load_dotenv
import os

load_dotenv()

print("SECRET_KEY:", os.getenv("SECRET_KEY"))
print("DATABASE_URL:", os.getenv("DATABASE_URL"))