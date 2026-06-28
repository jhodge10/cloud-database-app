from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

try:
    client = MongoClient(os.getenv("MONGO_URI"))
    client.admin.command("ping")
    print("✅ Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("❌ Failed to connect to MongoDB Atlas")
    print(e)

db = client[os.getenv("DATABASE_NAME")]
tasks_collection = db[os.getenv("COLLECTION_NAME")]

@app.route("/")
def home():
    return "<h1>Cloud To-Do List Connected!</h1>"

if __name__ == "__main__":
    app.run(debug=True)