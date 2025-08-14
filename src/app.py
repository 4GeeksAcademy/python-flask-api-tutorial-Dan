from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{"label": "Primera Tarea", "done": False}]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)

# Nuevo endpoint DELETE /todos
@app.route('/todos', methods=['DELETE'])
def delete_todo():
    request_body = request.get_json(force=True)
    position = request_body.get("position")

    if position is None or position < 0 or position >= len(todos):
        return 'Error: posición fuera de rango', 404

    todos.pop(position)
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)