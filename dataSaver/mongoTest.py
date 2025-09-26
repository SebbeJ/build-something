from pymongo import MongoClient
import redis
import datetime
import json

# Connect to MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client.myapp
collection = db.data

r = redis.Redis(host='redis', port=6379, db=0)

def save_data(data):
    # Sample data to save
    data = {
        'message': 'Hello from Python!',
        'timestamp': datetime.datetime.now(),
        'user_id': 12345,
        'tags': ['python', 'mongodb', 'docker'],
        'metadata': {
            'version': '1.0',
            'processed': True
        }
    }
    
    # Insert data
    result = collection.insert_one(data)
    print(f"Data saved with ID: {result.inserted_id}")
    
    return result.inserted_id

def get_all_data():
    # Retrieve all data
    documents = collection.find()
    print("\nAll documents in collection:")
    for doc in documents:
        print(f"ID: {doc['_id']}")
        print(f"Message: {doc['message']}")
        print(f"Timestamp: {doc['timestamp']}")
        print("---")

def search_data(query):
    # Search for specific data
    documents = collection.find(query)
    print(f"\nSearching for: {query}")
    for doc in documents:
        print(f"Found: {doc['message']}")

if __name__ == "__main__":
    #Recieve url

    # Get data

    #Save data to MongoDB (name and text)
    data_to_save = {
        'name': 'Sample Name',
        'text': 'This is a sample text.'
    }
    save_data(data_to_save)


    #Save data to redis (name)
    r.rpush('text_names', data_to_save['name'])