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
    request_body = request.json
    if request_body:
       new_todo={
          "label": request_body.get("label", ""),
          "done":request_body.get("done", False)
       }
       todos.append(new_todo)
       return jsonify(todos), 201
    else:
       return "Invalid request body", 400
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'











if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)