import requests

def main():
    #API URL
    url = "https://api.example.com"  
    #要传递的查询参数
    params = {
        "param1": "value1",
        "param2": "value2"
    }  
    try:
        response = requests.get(url, params=params)
        # 处理API成功响应
        if response.status_code == 200:    
            print("API Response:")
            print(response.json())
        # 处理API错误响应
        else:
            print(f"API returned error: {response.status_code} - {response.text}")
    # 处理请求异常
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

if __name__ == "__main__":
    main()
