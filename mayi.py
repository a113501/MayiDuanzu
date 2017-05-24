import requests
import regex as re

class app():

    def start(self, url):
        rooms_id = set()
        for offset_id in range(1,40):
            print("爬取页数")
            list = self.getpage(url,offset_id)
            while len(list)!=0:
                for room_id in list:
                    rooms_id.add(int(room_id['id']))

        print(len(rooms_id))

    def getpage(self,url,offset_id):
        allcity = requests.get('http://www.mayi.com/wap/getListOfOpenAndHot/')
        ajax = "http://m.mayi.com/ajax/searchmore/"
        data = {"offset":str(offset_id),
                "query_str":"shanghai",
                "d1":"2017-05-24",
                "d2":"2017-05-31"
                }
        s = requests.Session()
        user_agent = [
            "Mozilla/5.0 (Linux; Android 6.0.1; ONEPLUS A3000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",  ##OnePlus 6.0.1 Chrome
            "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30",  ##乐视X501 UC浏览器
            "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36",  ##乐视X501 Chrome浏览器
            "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 5.1.1)",  ##vivo X6S 百度浏览器
            "Mozilla/5.0 (Linux; Android 4.4.4; HM 2A Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036215 Safari/537.36 V1_AND_SQ_6.3.1_350_YYB_D QQ/6.3.1.2735 NetType/4G WebP/0.3.0 Pixel/720"
        ##红米手机2A 手机端QQ中直接打开（带4G标示）
        ]
        headers = {'user-agent': user_agent[0]}
        list = s.post(ajax,data=data,headers=headers)
        rooms_id = list.json()['data']
        return rooms_id
    def parse(self):
        pass
    def saver(self):
        pass


if __name__=='__main__':
    url = "http://m.mayi.com"
    mayi = app()
    mayi.start(url)
