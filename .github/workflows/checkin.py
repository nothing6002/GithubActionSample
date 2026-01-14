import requests
# 设置目标 URL
login_url = 'https://www.kungal.com/api/user/login'

# 构造登录数据
login_data = {
    "name": "电子文盲",
    "password": "15865242987Zkl"
}

# 设置完整的请求头（来自 cURL 抓包）
headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://www.kungal.com",
    "Referer": "https://www.kungal.com/login",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Sec-Ch-Ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=1, i"
}
# 创建 Session 对象发送请求
session = requests.Session()

# 发送 POST 登录请求
response = session.post(
    login_url,
    headers=headers,
    json=login_data
)
