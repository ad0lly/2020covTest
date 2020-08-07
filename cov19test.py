import datetime
import time
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def first_daily():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign&callback=&_=%d' % int(time.time() * 1000)
    data = json.loads(requests.get(url=url).json()['data'])

    foreign_list = data['foreignList']
    print(data)
    print(data.keys())

    print(len(foreign_list))
    for item in foreign_list:
        print(item['name'], end="")
    else:
        print("\n")

    world = foreign_list
    for item in world:
        print(item)
    else:
        print("\n")

    data_list = list()  # 日期
    data_confirm = list()  # 累计
    data_confirmAdd = list()  # 新增
    data_dead = list()  # 死亡
    data_heal = list()  # 治愈

    for item in data:
        # month, day = item['date'].split('/')
        # data_list.append(datetime.strptime('2020-%s-%s' % (month, day), '%Y-%m-%d'))
        data_confirm.append(int(item['confirm']))
        data_confirmAdd.append(int(item['confirmAdd']))
        data_dead.append(int(item['dead']))
        data_heal.append(int(item['heal']))
        return data_list, data_confirm, data_confirmAdd, data_dead, data_heal


def plt_daliy():
    data_list, data_confirm, data_confirmAdd, data_dead, data_heal = first_daily()
    plt.figure('2019-nCoV世界疫情统计图表', facecolor='#f4f4f4', figsize=(10, 8))
    plt.title('2019-nCoV世界疫情曲线', fontsize=20)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.plot(data_list, data_confirm, 'r-', label='确诊')
    plt.plot(data_list, data_confirm, 'rs')
    plt.plot(data_list, data_confirmAdd, 'b-', label='新增')
    plt.plot(data_list, data_confirmAdd)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # 格式化时间轴标注
    plt.gcf().autofmt_xdate()  # 优化标注（自动倾斜）
    plt.grid(linestyle=':')  # 显示网格
    plt.legend(loc='best')  # 显示图例
    plt.savefig('2019-nCoV疫情曲线.png')  # 保存为文件
    plt.show()


if __name__ == '__main__':
    plt_daliy()
