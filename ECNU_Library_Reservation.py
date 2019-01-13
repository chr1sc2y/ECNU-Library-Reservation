import os
import json
import requests
import datetime


class LibraryReserve:
    urls = ["http://202.120.82.2:8081/ClientWeb/pro/ajax/login.aspx",
            "http://202.120.82.2:8081/ClientWeb/pro/ajax/reserve.aspx"]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    user_info = {"act": "login"}
    time_info = {"dev_id": "3676547", "lab_id": "3674920",
                 "kind_id": "3675133", "type": "dev",
                 "act": "set_resv", "_": "1547215554524"}
    config_file = "./config.json"
    year, month, day = 0, 0, 0
    info = {}

    result_info = []
    num = 0

    def __init__(self):
        pass

    def Run(self):
        self.Reserve()
        self.PrintResult()

    def Reserve(self):
        file = open(self.config_file, 'r')
        info = json.load(file)
        self.info = info

        # set user id and password
        self.user_info['id'] = info['id']
        self.user_info['pwd'] = info['pwd']

        # output user info
        self.result_info.append("user info : \n")
        for key, value in self.user_info.items():
            self.result_info.append(key+' = ' + value+'\n')

        # login
        login_post = requests.post(url=self.urls[0],
                                   data=self.user_info,
                                   headers=self.headers)
        user_cookie = login_post.cookies

        # output login info
        self.result_info.append("login_post = "+str(login_post)+'\n')
        self.result_info.append("login_post.text = "+login_post.text+'\n')
        self.result_info.append("user_cookie = "+str(user_cookie)+'\n')

        # set reservation time
        day_after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)
        self.year = str(day_after_tomorrow.year)
        self.month = str(day_after_tomorrow.month)
        self.day = str(day_after_tomorrow.day)
        start_time_list = info['start time']
        end_time_list = info['end time']
        n = len(start_time_list)
        for i in range(n):
            start = str(self.year) + '-' + str(self.month) + '-' + \
                str(self.day) + ' ' + start_time_list[i]
            end = str(self.year) + '-' + str(self.month) + '-' + \
                str(self.day) + ' ' + end_time_list[i]
            self.time_info['start'] = start
            self.time_info['end'] = end
            start_time = start[start.find(
                ' ') + 1:start.find(':')] + start[start.find(':') + 1:]
            end_time = start[start.find(
                ' ') + 1:start.find(':')] + end[start.find(':') + 1:]
            self.time_info['start_time'] = start_time
            self.time_info['end_time'] = end_time

            # output time info
            self.result_info.append("\ntime info : \n")
            for key, value in self.time_info.items():
                self.result_info.append(key+' = ' + value+'\n')
            self.result_info.append('\n')

            # reserve rooms
            time_get = requests.get(url=self.urls[1],
                                    params=self.time_info,
                                    cookies=user_cookie,
                                    headers=self.headers)

            # output reserve info
            self.result_info.append("time_get = "+str(time_get)+'\n')
            self.result_info.append("time_get.text = "+time_get.text+'\n')

            # output result to console
            text = time_get.text
            output = text[text.find('msg":"') + 6:text.find('","data"')]
            print(output)

    def PrintResult(self):
        file_name = "./result" + "_" + \
            str(self.year) + '-' + str(self.month) + \
            '-' + str(self.day) + ".ign"
        file = open(file_name, 'w')
        file.writelines(self.result_info)
        del self.time_info['start_time']
        del self.time_info['end_time']
        del self.time_info['start']
        del self.time_info['end']
        self.result_info.clear()

libraryReserve = LibraryReserve()
libraryReserve.Run()
