# pip install flask


from flask import Flask, jsonify
import requests
import csv


# pip install flask

app = Flask(__name__)

def get_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()
        return comments
    else:
        return {"error": f"Falha na requisição. Código de status: {response.status_code}"}

@app.route('/api/comments', methods=['GET'])
def api_comments():
    comments = get_comments()
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)