from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/students', methods=['POST'])
def create_student():
    req = request.json
    print(req["name"])
    return { "id": "fix-me", "name": "fix-me" }, 201