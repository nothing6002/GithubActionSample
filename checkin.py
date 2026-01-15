import requests
import os
import time
import sys

# 从环境变量读取用户名和密码
USERNAME = os.environ.get('KUNGAL_USERNAME')
PASSWORD = os.environ.get('KUNGAL_PASSWORD')

if not USERNAME or not PASSWORD:
    print("错误: 未设置用户名或密码环境变量")
    sys.exit(1)

def main():
    session = requests.Session()
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://www.kungal.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # 使用环境变量，而不是硬编码
    login_data = {
        "name": USERNAME,
        "password": PASSWORD
    }
    
    print("正在登录...")
    login_response = session.post(
        'https://www.kungal.com/api/user/login',
        headers=headers,
        json=login_data
    )
    
    print(f"登录状态码: {login_response.status_code}")
    
    if login_response.status_code != 200:
        print(f"登录失败: {login_response.text}")
        return
    
    print("登录成功，正在签到...")
    
    # 发送签到请求
    checkin_response = session.post('https://www.kungal.com/api/user/check-in')
    print(f"签到状态码: {checkin_response.status_code}")
    
    # 记录结果
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    if checkin_response.status_code == 200:
        points = checkin_response.text
        result = f"{timestamp} - 签到成功! 获得点数: {points}"
        print(result)
    elif checkin_response.status_code == 233:
        result = f"{timestamp} - 今日已签到过"
        print(result)
    else:
        result = f"{timestamp} - 签到失败: {checkin_response.text}"
        print(result)
    
    # 写入日志文件（用于上传为artifact）
    with open('checkin_history.txt', 'a') as f:
        f.write(result + "\n")

if __name__ == "__main__":
    main()
