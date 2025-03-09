from flask import Flask, jsonify
from http.server import BaseHTTPRequestHandler

app = Flask(__name__)

@app.route('/api1', methods=['GET'])
def api1():
    data = {
        "课程销量": {
            "F课程": 15324,
            "G课程": 355,
        },
    }
    
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api2', methods=['GET'])
def api2():
    data = {
        "课程销量": "这个api返回课程销量数据",
        "F课程": 15324,
        "G课程": 355
    }
    
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api3', methods=['GET'])
def api3():
    data = {
        "F课程和G课程的定价、上线时长、销量、好评率": "索引字段",
        "课程运营信息": {
            "F课程": {
                "定价": "99元",
                "上线时长": "3年",
                "销量": 15324,
                "好评率": "98%",
            },
            "G课程": {
                "定价": "129元",
                "上线时长": "1年",
                "销量": 355,
                "好评率": "97.5%",
            }
        }
    }
    
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api4', methods=['GET'])
def api4():
    data = {
        "索引字段": "F课程、G课程",
        "课程运营信息": {
            "F课程": {
                "定价": "99元",
                "上线时长": "3年",
                "销量": 15324,
                "好评率": "98%",
            },
            "G课程": {
                "定价": "129元",
                "上线时长": "1年",
                "销量": 355,
                "好评率": "97.5%",
            }
        }
    }
    
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API服务正常运行中", "endpoints": ["/api1", "/api2", "/api3", "/api4"]}), 200

# 为Vercel无服务器函数创建处理程序
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 将请求路径传递给Flask应用
        from io import StringIO
        import sys
        
        # 捕获输出
        output = StringIO()
        sys.stdout = output
        
        # 处理请求
        response = app.handle_request(self.path)
        
        # 恢复标准输出
        sys.stdout = sys.__stdout__
        
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # 发送响应
        self.wfile.write(response.encode())
        return