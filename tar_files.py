import os, tarfile
import datetime
import requests
import logging
logger = logging.getLogger()
root_path = os.path.dirname(__file__)
tar_path = os.path.join(root_path, datetime.datetime.today().strftime('%Y-%m-%d'))
# 一次性打包整个根目录。空子目录会被打包。
# 如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。

def lixianxiazai(data_url):
    url = 'https://pan.baidu.com/rest/2.0/services/cloud_dl?channel=chunlei&web=1&app_id=250528&bdstoken=c45f192624488d9e0c4aa8bbe56370f4&logid=MTQ5NDkyNTIyNzg0OTAuMDk2NDM1NjcxNDI3MDQ2MDE=&clienttype=0'
    data = {'app_id': '250528',
     'method': 'add_task',
     'save_path': '/back_save/',
     'source_url': data_url}
    cookies = {'BAIDUID': '89EBE560C684D775B6E18436DEBF98B5:FG=1',
     'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
     'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
     'BDSFRCVID': 'akusJeCCxG3uirQZyu9ZSQ0fvf6-zkKQYWkr3J',
     'BDUSS': '1kdWFUSGpxWDVISXgwUVB-QXBQa0pQajBKdjNZNDVVTEdwUzB4ZHBoOHduaDVaSVFBQUFBJCQAAAAAAAAAAAEAAACWC9wtcXVuMTUwMTAyNzkzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAR91gwEfdYMC',
     'BIDUPSID': '89EBE560C684D775B6E18436DEBF98B5',
     'H_BDCLCKID_SF': 'tR-tVCIMJKt3enO1hnofqR_Lqxby26ntB25eaJ5nJDohE4n_2R5A2tAwXboMy-tLQR5N-qrlQpP-hK56XxtVhfFjMG3Nq6vX-ItjKl0MLPjtbb0xynoDhn-bjxnMBMPjamOnaU5KLIFabnO1hnofq4D_MfOtetJyaR3KB-5bWJ5TEPnjDnoEKl_l2q_8XqJItIcq0DLEMJvvVfT5MnK5y6ISKx-_J6k8tRvP',
     'H_PS_PSSID': '1444_13289_21087_20719',
     'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0': '1494925178',
     'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0': '1493688777,1494207361,1494924938,1494925178',
     'PANPSC': '17031273811792059133%3AWaz2A%2F7j1vXIva6S63mexN3kfeOZ%2BBP3Z%2FqoV88oV8HrkW89kGelBIM6La9EbgvRqPl%2FPqKdYnZ4HF6HKY%2FEB94LZosfYbqC7MXF2oQEWbi2%2BIvyRfcH%2BHj7YdpwIDfJOy6S0zDqC6VtUVw2SfQVPqO2GhXGA0dK',
     'PANWEB': '1',
     'PSINO': '1',
     'PSTM': '1492060932',
     'SCRC': '1b3f6295cf9bfe178129d09308209fb3',
     'SFSSID': '1lenf8892mhmcn8kfp9v2d3hr6',
     'SIGNIN_UC': '70a2711cf1d3d9b1a82d2f87d633bd8a02449378733',
     'STOKEN': '40498b67d4a48f5ed70347dd3ef2641d6f0fadf0f02687de76b0bc3d968fa9bd',
     '__cfduid': 'dcc7efa827bfa41a7d293dd6b148775431492586981',
     'bdshare_firstime': '1488348041878',
     'cflag': '15%3A3',
     'pan_login_way': '1',
     'panlogin_animate_showed': '1',
     'secu': '1',
     'uc_login_unique': '6e62f849e3c74041a251ca0ddc72278f'}
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
     'Accept-Encoding': 'gzip, deflate, br',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'Connection': 'keep-alive',
     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
     'Origin': 'https://pan.baidu.com',
     'Referer': 'https://pan.baidu.com/disk/home',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3013.3 Safari/537.36',
     'X-Requested-With': 'XMLHttpRequest'}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)
    logger.debug(r.text)



def make_targz(source_dir, output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == '__main__':
    bf_list = ['/home/liuchang/764191074/']
    for k, d in enumerate(bf_list):
        make_targz(d, tar_path + '-{}.tar'.format(k))
        lixianxiazai()