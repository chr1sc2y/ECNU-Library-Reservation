import os
import json
import requests


class LibraryReserve:
    urls = ["http://202.120.82.2:8081/ClientWeb/pro/ajax/login.aspx",
            "http://202.120.82.2:8081/ClientWeb/pro/ajax/reserve.aspx"]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    user_info = {"act": "login"}
    time_info = {"dev_id": "3676547", "lab_id": "3674920", "kind_id": "3675133",
                 "type": "dev", "act": "set_resv",
                 "_": "1547215554524"}
    result_info = []
    num = 0

    def __init__(self):
        pass

    def Run(self):
        files = os.listdir("./reservations")
        for file in files:
            if not os.path.isdir(file):
                name = str(file)
                if(name == ".DS_Store"):
                    continue
                num = name[name.find('_') + 1:name.find('.')]
                self.ConcatInfo("./reservations/" + file)
                self.Reserve()
                self.Result(num)

    def ConcatInfo(self, config_file):
        file = open(config_file, 'r')
        info = json.load(file)
        self.user_info['id'] = info['student ID']
        self.user_info['pwd'] = info['password']

        start_str = info['start time']
        end_str = info['end time']
        self.time_info['start'] = start_str
        self.time_info['end'] = end_str
        start_time = start_str[start_str.find(
            ' ') + 1:start_str.find(':')] + start_str[start_str.find(':') + 1:]
        end_time = start_str[start_str.find(
            ' ') + 1:start_str.find(':')] + end_str[start_str.find(':') + 1:]
        self.time_info['start_time'] = start_time
        self.time_info['end_time'] = end_time

        self.result_info.append("user info : \n")
        for key, value in self.user_info.items():
            self.result_info.append(key+' = ' + value+'\n')
        self.result_info.append("\ntime info : \n")
        for key, value in self.time_info.items():
            self.result_info.append(key+' = ' + value+'\n')
        self.result_info.append('\n')

    def Reserve(self):
        login_post = requests.post(url=self.urls[0],
                                   data=self.user_info,
                                   headers=self.headers)
        user_cookie = login_post.cookies
        self.result_info.append("login_post = "+str(login_post)+'\n')
        self.result_info.append("login_post.text = "+login_post.text+'\n')
        self.result_info.append("user_cookie = "+str(user_cookie)+'\n')

        time_get = requests.get(url=self.urls[1],
                                params=self.time_info,
                                cookies=user_cookie,
                                headers=self.headers)
        self.result_info.append("time_get = "+str(time_get)+'\n')
        self.result_info.append("time_get.text = "+time_get.text+'\n')

        text = time_get.text
        output = text[text.find('msg":"') + 6:text.find('","data"')]
        print(output)

    def Result(self, num):
        file_name = "./results/"+"result_" + str(num) + ".md"
        file = open(file_name, 'w')
        file.writelines(self.result_info)
        del self.user_info['id']
        del self.user_info['pwd']
        del self.time_info['start_time']
        del self.time_info['end_time']
        del self.time_info['start']
        del self.time_info['end']
        self.result_info.clear()


libraryReserve = LibraryReserve()
libraryReserve.Run()
