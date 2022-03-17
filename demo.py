import time

import requests


class Pupu():
    # 伪装自己,冒充成微信小程序
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    # 需要访问的地址
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/ed60af11-25b0-48b8-bc5b-f9136d9f89ad'

    # 从url中得到json数据
    response = requests.get(url, headers=headers).json()

    def getmessage(self):
        # 从json中获取需要的数据
        data = self.response['data']
        specification = data['spec']
        price = data['price'] / 100
        discount_price = data['market_price'] / 100
        describtion = data['share_content']
        product = data['share_title']
        print('--------------------商品:' + product + '--------------------')
        print('规格:' + specification)
        print('价格: ' + str(price))
        print('折扣价/原价: ' + str(price) + "/" + str(discount_price))
        print('详细内容:' + describtion)
        print('--------------------"' + product + '"的价格波动--------------------')

        # 间隔一秒钟获取当前商品的价格
        for content in range(6):
            print('当前时间为' + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + '价格为' + str(price))
            time.sleep(1)


if __name__ == '__main__':
    pupu = Pupu()
    pupu.getmessage()