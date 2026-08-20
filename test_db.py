from app import app
from extensions import db
from sqlalchemy import text

with app.app_context():
    try:
        result = db.session.execute(text("SELECT version();"))
        print("✅ Connected successfully!")
        print(result.fetchone()[0])
    except Exception as e:
        print("❌ Connection failed")
        print(type(e).__name__)
        print(e)