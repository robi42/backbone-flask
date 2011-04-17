from flask import Flask, render_template, request, make_response, json, jsonify
from models import Todo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos')
def retrieve_todos():
    content = json.dumps([dict(id=todo.key().id(),
                               content=todo.content,
                               done=todo.done,
                               order=todo.order) for todo in Todo.all()])
    response = make_response(content)
    response.mimetype = 'application/json'
    return response

@app.route('/todos', methods=['POST'])
def create_todo():
    data = json.loads(request.data)
    todo = Todo(content=data['content'], done=data['done'], order=data['order'])
    todo.put()
    response = make_response(jsonify(id=int(todo.key().id()),
                                     content=todo.content,
                                     done=todo.done,
                                     order=todo.order))
    response.mimetype = 'application/json'
    return response

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.get_by_id(id)
    data = json.loads(request.data)
    todo.content = data['content']
    todo.done = data['done']
    todo.save()
    response = make_response(jsonify(id=id,
                                     content=todo.content,
                                     done=todo.done))
    response.mimetype = 'application/json'
    return response

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.get_by_id(id)
    todo.delete()
    response = make_response()
    response.mimetype = 'application/json'
    return response
