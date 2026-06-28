from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
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
    tasks = list(tasks_collection.find())
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)