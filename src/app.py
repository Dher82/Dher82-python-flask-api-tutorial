from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    try:
        new_todo = request.get_json()
        todos.append(new_todo)
        return jsonify(todos)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/todos/<int:position_id>', methods=['DELETE'])
def delete_todo(position_id):
    try:
        
        if position_id >= 0 and position_id < len(todos):
            
            todos.pop(position_id)
            return jsonify(todos)
        else:
            return jsonify({"error": "Position out of range"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400










if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
