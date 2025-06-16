from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 模擬資料庫
accounts = [
    {
        "name": "李佑仁",
        "rate": 1,
        "records": [
            {"date": "2024-01-01", "type": "存入", "amount": 2000}
        ]
    }
]

@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    return jsonify(accounts)

@app.route('/api/accounts', methods=['POST'])
def add_account():
    data = request.json
    accounts.append({
        "name": data["name"],
        "rate": data["rate"],
        "records": []
    })
    return jsonify({"status": "ok"}), 201

@app.route('/api/accounts/<int:idx>', methods=['PUT'])
def update_account(idx):
    data = request.json
    if 0 <= idx < len(accounts):
        accounts[idx] = data
        return jsonify({"status": "ok"})
    return jsonify({"error": "not found"}), 404

@app.route('/api/accounts/<int:idx>', methods=['DELETE'])
def delete_account(idx):
    if 0 <= idx < len(accounts):
        accounts.pop(idx)
        return jsonify({"status": "ok"})
    return jsonify({"error": "not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
