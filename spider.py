# coding: utf-8

import requests
import redis


class CCNUSpider(object):
    """
    CCNU 爬虫...
    """
    def get_stu_id(self, start_id, end_id):
        """
        输入学号范围(以字符串形式输入)
        获取对应学号的用户名数据
        将学号用户名存储到redis数据库中
        采用 {用户名:学号} 键值存储
        """
        print "--->---->---开始CCNU爬取--->--->--->"
        get_url = "API_URL"
        for id in range(int(start_id), int(end_id)):
            res = requests.get(get_url % id)
            if (res.json() == None):
                id = id + 1
            else:
                stu = res.json()[0].get(u'userName')
                pool = redis.ConnectionPool(host="hostname", port=port, db=0)
                r = redis.Redis(connection_pool = pool)
                r.set(stu, id)
                r.save()
                print "%s ---> ok" % id
        print "---->数据保存在服务器硬盘上, 爬取完毕--->"


if __name__ == "__main__":
    spider = CCNUSpider()
    start_id = raw_input('\_起始学号范围: ')
    end_id =  raw_input('\_截止学号范围+1: ')
    spider.get_stu_id(start_id, end_id)

