from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

user_db = {
    "admin": "123456",
    "user01": "666666",
    "test": "test123"
}

# 首页测试
@app.route("/", methods=["GET"])
def index():
    return "后端服务正常，登录接口 POST /api/login"

# 登录接口路径，只能写 /api/login
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"code": 400, "msg": "账号密码不能为空"})
    if username not in user_db:
        return jsonify({"code": 401, "msg": "账号不存在"})
    if user_db[username] != password:
        return jsonify({"code": 402, "msg": "密码错误，请重新输入"})

    return jsonify({
        "code": 200,
        "msg": "登录成功",
        "redirectUrl": "success.html"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)