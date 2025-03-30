from flask import Flask, render_template, request, jsonify
from taskDAO import taskDAO
from taskDTO import taskDTO

app = Flask(__name__)

@app.route('/')
def index():
    tasks = taskDAO.list()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    name = data.get('name')
    status = data.get('status', False)  # Mặc định là False
    task = taskDTO(None, name, status)
    if taskDAO.insert(task):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False}), 500

@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()  # Lấy dữ liệu gửi từ client dưới dạng JSON
    id = data.get('id')
    print("ID nhận được:", id)
    if id is None:
        return jsonify({"success": False, "error": "No task id provided"}), 400

    # Tạo TaskDTO chỉ cần id, các trường khác có thể để None
    task = taskDTO(id, None, None)
    if taskDAO.delete(task):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False}), 500
    
@app.route('/update_task', methods=['POST'])
def update_task():
    data = request.get_json()
    task_id = data.get('id')
    status = data.get('status')
    if task_id is None or status is None:
        return jsonify({"success": False, "error": "Thiếu thông tin"}), 400

    task = taskDTO(task_id, None, status)
    if taskDAO.update(task):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
