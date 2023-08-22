import requests
import matplotlib.pyplot as plt

def get_city_id():
    #city_name = input("请输入你想要查询天气的城市名字：")
    #通过输入的名字获取到指定的ID
    city_id = str(101220101)
    return city_id

def get_weather_info(city_id):
    url = "http://t.weather.sojson.com/api/weather/city/" + city_id
    print(url)
    response = requests.get(url).json()
    cityInfo = response.get('cityInfo')
    print(cityInfo)
    forecast = response.get('data').get('forecast')
    x_date = []
    y_high = []
    y_low = []
    for info in forecast:
        #print(info)
        x_date.append(info.get('date'))
        y_high.append(int(info.get('high')[3:-1]))
        y_low.append(int(info.get('low')[3:-1]))
    #画温度折线图
    return x_date, y_high, y_low

def temperature_forecast(x_date, y_high, y_low):
    # 画出高温度曲线
    plt.figure('Temperature')
    plt.plot(x_date, y_high, color='red', label='high')
    #点出每个时刻的温度点
    plt.scatter(x_date, y_high, color='red')
    #画出低温度曲线
    plt.plot(x_date, y_low, color='blue', label='low')
    #点出每个时刻的温度点
    plt.scatter(x_date, y_low, color='blue')
    #添加注释
    plt.legend()
    #添加标题
    plt.title("Temperature Prediction of Heifei in 2 Weeks")
    #x轴数据
    plt.xlabel("Date")
    #y轴数据
    plt.ylabel("temperature/°C")
    # 显示网格线
    plt.grid(True)
    # 显示图形
    plt.show()

def main():
    city_id = get_city_id()
    x_date, y_high, y_low = get_weather_info(city_id)
    temperature_forecast(x_date, y_high, y_low)

if __name__ == '__main__':
    main()
