from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
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

@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title")

    if title.strip():

        tasks_collection.insert_one({
            "title": title,
            "completed": False
        })

    return redirect(url_for("home"))

@app.route("/edit/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    task = tasks_collection.find_one({"_id": ObjectId(task_id)})

    if request.method == "POST":

        title = request.form.get("title")

        completed = "completed" in request.form

        tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {
                "$set": {
                    "title": title,
                    "completed": completed
                }
            }
        )

        return redirect(url_for("home"))

    return render_template("edit.html", task=task)

@app.route("/delete/<task_id>")
def delete_task(task_id):

    tasks_collection.delete_one(
        {
            "_id": ObjectId(task_id)
        }
    )

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)