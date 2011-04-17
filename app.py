from flask import Flask, render_template, request, make_response, json, jsonify
from models import Todo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET', 'POST'])
def create_or_retrieve_todos():
    if request.method == 'POST':
        return create_todo()
    else:
        return retrieve_todos()

@app.route('/todos/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_todo(id):
    if request.method == 'PUT':
        return update_todo(id)
    else:
        return delete_todo(id)

def create_todo():
    data = json.loads(request.data)
    todo = Todo(content=data['content'], done=data['done'], order=data['order'])
    todo.put()
    return jsonify(id=int(todo.key().id()),
                   content=todo.content,
                   done=todo.done,
                   order=todo.order)

def retrieve_todos():
    content = json.dumps([dict(id=todo.key().id(),
                               content=todo.content,
                               done=todo.done,
                               order=todo.order) for todo in Todo.all()])
    response = make_response(content)
    response.mimetype = 'application/json'
    return response

def update_todo(id):
    todo = Todo.get_by_id(id)
    data = json.loads(request.data)
    todo.content = data['content']
    todo.done = data['done']
    todo.save()
    return jsonify(id=id, content=todo.content, done=todo.done)

def delete_todo(id):
    todo = Todo.get_by_id(id)
    todo.delete()
    return jsonify()
