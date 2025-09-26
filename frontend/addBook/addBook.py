from flask import Flask, request, render_template_string
# import urllib.request
# from redis import Redis
# import json
import requests

# redis = Redis(host='redis', port=6379)


app = Flask(__name__)

# HTML template
with open("frontend.txt", "r") as file:
    page_template = file.read()

def send_url(name, url):
    try:
        response = requests.post('http://dataSaver:5000/dataSaver/save', json={'name': name, 'url': url})
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending to dataSaver/save: {e}")
        return None

@app.route("/add", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_url = request.form.get("bookURL")
        user_book = request.form.get("bookName")

        response = send_url(user_book, user_url)

    return render_template_string(page_template, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)