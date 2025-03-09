from flask import Flask, jsonify, Request, Response
import json

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

# Vercel无服务器函数入口点
# 修改handler函数
def handler(request, response):
    # 获取请求路径
    path = request.path
    
    # 根据路径返回不同的数据
    if path == "/api1":
        data = {
            "课程销量": {
                "F课程": 15324,
                "G课程": 355,
            },
        }
    elif path == "/api2":
        data = {
            "课程销量": "这个api返回课程销量数据",
            "F课程": 15324,
            "G课程": 355
        }
    elif path == "/api3":
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
    elif path == "/api4":
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
    else:
        data = {"message": "API服务正常运行中", "endpoints": ["/api1", "/api2", "/api3", "/api4"]}
    
    # 创建响应
    response.status = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return json.dumps(data, ensure_ascii=False)