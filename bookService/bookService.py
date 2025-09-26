from pymongo import MongoClient
import redis

client = MongoClient('mongodb://mongo:27017/')
db = client.myapp
collection = db.data

def search_data(query):
    # Search for specific data
    documents = collection.find(query)
    return documents

def find_closest_word(formatted_sentences):
    text = "This is a sample text."
    sentence_place = float('inf')
    min_distance = float('inf')
    for sentence in formatted_sentences:
        if sentence['distance'] < min_distance:
            min_distance = sentence['distance']
            text = sentence['text']
            sentence_place = sentence['place']
        elif sentence['distance'] == min_distance and sentence['place'] < sentence_place:
            text = sentence['text']
            sentence_place = sentence['place']
    
    return {'text': text, 'distance': min_distance, 'place': sentence_place}

# if __name__ == "__main__":
    #Register in service registry

    # while True:


    #     #Recieve name of book (Detta kommer nog hämtas från samma objekt sen)
    #     name = "Sample Book"
    #     query = "Sample Query"

    #     #Collect book
    #     book_query = {'name': name}
    #     documents = search_data(book_query)

    #     text = ""
    #     sentences = []
    #     if documents.count() == 0:
    #         print("No book found with that name.")
    #     elif documents.count() > 1:
    #         print("Multiple books found with that name.")
    #     else:
    #         book = documents[0]
    #         print(f"Book found: {book['name']}")
    #         #Process book
    #         text = book['text']
    #         sentences = text.split('. ')
    #         print(f"Book has {len(sentences)} sentences.")

    #     #Send segments to sentence services
    #     for i in range(len(sentences)):
    #         sentence = sentences[i]
    #         location = str(i)
    #         #Send sentence, query and location to sentence service

    #     #Recieve answers
    #     formatted_sentences = []

    #     #Compile and find closes word in the first sentence
    #     closest_match = find_closest_word(formatted_sentences)

        #Send answer back to requester

        #Register to service registry again

