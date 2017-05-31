#! /urs/bin/env python3
# coding=utf-8
import traceback
import MySQLdb.cursors
import logging
from block_timer.timer import Timer
import pprint
import threading
import requests


class GetTmpChexIP(threading.Thread):
    return_ip = []
    test_url_list = set()
    over_flag = list()
    ip_list = []

    def __init__(self, ip=''):
        threading.Thread.__init__(self)
        self.ip = ip

    def get_proxy_from_mysql(self):
        try:
            conn = MySQLdb.connect(host='192.3.244.150', user='ip_proxy_user', passwd='lc4771822', db='ip_proxy', port=3306,
                                   use_unicode=True, charset='utf8mb4', cursorclass=MySQLdb.cursors.DictCursor)
            cursor = conn.cursor()
            sql = 'SELECT * FROM httpbin WHERE speed > 0 and speed < 6 AND vali_count >1 ORDER BY id '
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                return list(results)
            except Exception as e:
                conn.rollback()
                traceback.print_exc()
                return []
        except:
            traceback.print_exc()
        finally:
            conn.close()

    def chex(self):
        if self.ip:
            proxies = {
                'http': 'http://{}'.format(self.ip),
                'https': 'http://{}'.format(self.ip)
            }

            url = 'http://www.qichacha.com/firm_CN_8b18d454aae71b3de93abe084b8623a1'
            try:
                headers = {'Accept': 'text/html, */*; q=0.01',
                                     'Accept-Language': 'zh-CN,zh;q=0.8',
                                     'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                                     'X-Requested-With': 'XMLHttpRequest'}
                r = requests.get(url, proxies=proxies, headers=headers, timeout=5)
            except requests.exceptions.ProxyError:
                return False
            except requests.exceptions.SSLError:
                return False
            except requests.exceptions.ConnectTimeout:
                return False
            except requests.exceptions.ConnectionError:
                return False
            except:
                return False

            if r.status_code == 200 and '91110116589133454J' in r.text:
                print(self.ip)
                return True
            else:
                return False

    def run(self):
        self.over_flag.append(self.name)
        try:
            if self.chex():
                self.return_ip.append(self.ip)
        except:
            print(traceback.format_exc())
        self.over_flag.remove(self.name)


def GetImageUrl():
    with Timer() as t:
        g = GetTmpChexIP()
        g.ip_list = ['{ip}:{port}'.format(**i) for i in g.get_proxy_from_mysql()]
        for ip in g.ip_list:
            x = GetTmpChexIP(ip)
            x.start()

        while g.over_flag:
            pass

        return g.return_ip


if __name__ == '__main__':
    pprint.pprint(GetImageUrl())