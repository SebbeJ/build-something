from flask import Flask, request, render_template_string, jsonify
import requests

app = Flask(__name__)

# HTML template with a question
with open("frontend-query.txt", "r") as file:
    page_template_query = file.read()

with open("frontend-add.txt", "r") as file:
    page_template_add = file.read()

def sendQuery(data):
    try:
        # print(f'Sending to data/search, data type: {type(data)}')
        response = requests.post('http://dataSaver:5000/dataSaver/search', json={'name': data})
        # print(f'recived {response.json()}')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending to dataSaver/search: {e}")
        return None
    
def send_url(name, url):
    try:
        response = requests.post('http://dataSaver:5000/dataSaver/save', json={'name': name, 'url': url})
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending to dataSaver/save: {e}")
        return None

@app.route("/add", methods=["GET", "POST"])
def add():
    response = None
    if request.method == "POST":
        user_url = request.form.get("bookURL")
        user_book = request.form.get("bookName")

        send_url(user_book, user_url)
        response = "Sucssess!"

    return render_template_string(page_template_add, response=response)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_input = request.form.get("statement")
        # response = f"Intresting indeed, {user_input}"
        response = sendQuery(user_input)
        # print(f'query {response}')


    return render_template_string(page_template_query, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
