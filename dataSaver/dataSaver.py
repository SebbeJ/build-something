from pymongo import MongoClient
from flask import request, Flask, jsonify
import urllib.request

# Connect to MongoDB
client = MongoClient('mongodb://mongodb-service:27017/')
db = client.myapp
collection = db.data


app = Flask(__name__)

@app.route("/dataSaver/save", methods = ['POST'])
def save_data():
    params = request.json

    # with urllib.request.urlopen(params["url"]) as web:
    #     content = web.read().decode('utf-8')

    book_name = params["name"]

    print(f'saver type name: {type(book_name)}')

    data = {"name": book_name, "content" : params["url"]}
    
    # Insert data
    result = collection.insert_one(data)
    print(f"saving data with name: {book_name}")
    print(f"Data saved with ID: {result.inserted_id}")
    
    return jsonify({
        "message": "Data saved successfully",
        "id": str(result.inserted_id)   # convert ObjectId → str
    }), 201


def get_all_data():
    # Retrieve all data
    documents = collection.find()
    print("\nAll documents in collection:")
    for doc in documents:
        print(f"ID: {doc['_id']}")
        print(f"Message: {doc['message']}")
        print(f"Timestamp: {doc['timestamp']}")
        print("---")

@app.route("/dataSaver/search", methods=["POST"])
def search_data():
    params = request.json
    print(f'search_data: {params}')

    if not params or "name" not in params:
        return jsonify({"error": "Missing 'name' field"}), 400

    query = {"name": params["name"]}

    print(f'search type name: {type(params["name"])}')

    print(f"\nSearching for: {query}")

    # Fetch a single document
    document = collection.find_one(query)

    if not document:
        return jsonify({"error": "No document found"}), 404

    # Extract only the "contents" field
    contents = document.get("content")
    print(f"Found contents: {contents}")

    return jsonify({"content": contents}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)