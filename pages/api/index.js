export default function handler(req, res) {
  const { method, url } = req;
  const path = url.split('?')[0];

  // 设置CORS头
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  // 根据路径返回不同的数据
  if (path === '/api/api1') {
    const data = {
      "课程销量": {
        "F课程": 15324,
        "G课程": 355,
      },
    };
    res.status(200).json(data);
  } 
  else if (path === '/api/api2') {
    const data = {
      "课程销量": "这个api返回课程销量数据",
      "F课程": 15324,
      "G课程": 355
    };
    res.status(200).json(data);
  } 
  else if (path === '/api/api3') {
    const data = {
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
    };
    res.status(200).json(data);
  } 
  else if (path === '/api/api4') {
    const data = {
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
    };
    res.status(200).json(data);
  } 
  else {
    const data = {
      "message": "API服务正常运行中",
      "endpoints": ["/api/api1", "/api/api2", "/api/api3", "/api/api4"]
    };
    res.status(200).json(data);
  }
}