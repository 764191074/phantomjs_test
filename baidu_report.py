# coding=utf-8
import requests
import logging
import json
import random
import traceback
from pyquery import PyQuery as pyq
import urllib.parse
<<<<<<< HEAD

def get_cookies_list():
    with open('baidu_code.txt', 'r') as f:
        lines=f.readlines()
    return_list = []
    for l in lines:
        l_list = l.split('----')
        return_list.append(l_list[-1])
    return return_list

cookies_list = get_cookies_list()
=======
#
>>>>>>> f0afc0269a0005bdbfa5323f97b2f903ae0a52c5

def get_tiem_url(baidu_cache_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3013.3 Safari/537.36'}
    r = requests.get(baidu_cache_url, headers=headers)
    try:
        jpy = pyq(r.content.decode(encoding='gbk', errors='ignore'))
    except:
        pass
    retun_time = jpy('#bd_snap_txt > span:nth-child(2)').text()
    retun_time = ' '.join(retun_time.split(' ')[1:3])
    return_url = jpy('#bd_snap_note > a').text()
    return retun_time, return_url


def get_url_list(keyword, num):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3013.3 Safari/537.36'}
        r = requests.get('https://www.baidu.com/s?wd={}&pn={}'.format(keyword, num), headers=headers)
        jpy = pyq(r.text)
        li_list = jpy('div.result.c-container ')
        return_list = []
        for li in li_list.items():
            a_list = li.find('a')
            title = a_list.eq(0).text()
            for a in a_list.items():
                # print(a.text())
                if a.text() == u'百度快照':
                    time_date, url = get_tiem_url(a.attr('href'))
                    print(keyword, url, time_date, title)
                    return_list.append([keyword, url, title, time_date])
            print('____________________________')
        return return_list
    except:
        logging.error(traceback.format_exc())
        logging.info('vars()\n{}\n{:30}'.format(vars(), '*'))
        return []


def report(description, keyword, surl, title):
    data = {'description': description,
             'hasGw': '0',
             'hasV': '0',
             'isnatural': '1',
             'keyword': keyword,
             'phone': '',
             'problemtype': '11001',
             'surl': surl,
             'title': title,
             'token': '',
             'upload': '',
             'url': ''
            }

    headers = {
         'Accept': '*/*',
         'Accept-Encoding': 'gzip, deflate',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'Connection': 'keep-alive',
         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'Origin': 'http://jubao.baidu.com',
         'Referer': 'http://jubao.baidu.com/jubao/accu/?surl=http%3A//tv%2Esohu%2Ecom/s2013/saintseiya/&token=F2770FB88FE6EF8B085F1D5D80978CEB&title=%E5%9C%A3%E6%96%97%E5%A3%AB%E6%98%9F%E7%9F%A2(%E5%9B%BD%E8%AF%AD%E7%89%88)-%E5%9C%A3%E6%96%97%E5%A3%AB%E6%98%9F%E7%9F%A2(%E5%9B%BD%E8%AF%AD%E7%89%88)%E5%85%A8%E9%9B%86(1-114%E5%85%A8)-..._%E6%90%9C%E7%8B%90%E8%A7%86%E9%A2%91&q=%E5%9C%A3%E6%96%97%E5%A3%AB%E6%98%9F%E7%9F%A2&has_gw=0&has_v=0',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3013.3 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'
           }
    cookies = {'BDUSS': random.choices(cookies_list)}
    url = 'http://jubao.baidu.com/jubao/accu/submit'
    r = requests.post(url, cookies=cookies, data=data, headers=headers)


def get_baidu_keyword(damain):
    r = requests.get('http://baidurank.aizhan.com/baidu/{}/'.format(damain))
    jpy = pyq(r.text)
    itmes = jpy('#tabcon_baidu_0 > table > tbody > tr')
    run_list = []
    for i in itmes.items():
        item = dict()
        a_tag = i('td.word > a')
        item['baidu_url'] = a_tag.attr('href')
        item['keyword'] = a_tag.text().strip()
        # paiming
        item['paiming'] = i('td.blue > span').text().strip()
        # zhishu
        item['zhishu'] = i('td:nth-child(3) > a').text() or i('td:nth-child(4) > a').text()
        run_list.append(item)
    return run_list
# damain = 'jijise.cn'
# for k in get_baidu_keyword(damain):
#
#     list_r = get_url_list(k['keyword'], 0)
#     for i in list_r:
#         if damain in i[1]:
#             break
#         print(i)
#         report('色情网站', i[0], i[1], i[2])



# headers = {'Referer': 'http://i.baidu.com/my/jubao'}
# cookies = {
#     'BDUSS': 'k1NOWNuczQxQlczWjJvLX5xVWZnamdXT1lIRjlZZXZwbC0zS3R3QVoxbXFUQjFaSVFBQUFBJCQAAAAAAAAAAAEAAAAglsWyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKq~9Viqv~VYZ;PTOKEN=bf98fe290ccdc6ca8174c0cb94d84428;STOKEN=599f13c9abfc45e1d8909e190b07e6b451ce7c61f1e8ebe2de5618df3e890487'}
# # &page=2
# r = requests.get("http://jubao.baidu.com/jubao/accu/listajax?&page=3", headers=headers, cookies=cookies)
# html_resou = r.text.replace('(', '').replace(')', '')
# json_data = json.loads(html_resou)
pass