# config.py 自定义配置
import os
import re

"""
github action部署或本地部署
从环境变量获取值,如果不存在使用默认本地值
每一次代表30秒，比如你想刷1个小时这里填120，你只需要签到这里填2次
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM', '120'))
# pushplus or telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# push-plus
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# 复制的curl_bath命令
curl_str = os.getenv('WXREAD_CURL')

# 对应替换
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
    "baggage": "sentry-environment=production,sentry-release=dev-1727596539903,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=d3cc3a94f5244647b8064ecd77eb8ba6",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "dnt": "1",
    "origin": "https://weread.qq.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://weread.qq.com/web/reader/ce032b305a9bc1ce0b0dd2akd2d32c50249d2ddea18fb39",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "d3cc3a94f5244647b8064ecd77eb8ba6-93b39e13fa4e5fd6",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
#
# #对应替换
cookies = {
    "RK": "oxEY1bTnXf",
    "ptcz": "53e3b35a9486dd63c4d06430b05aa169402117fc407dc5cc9329b41e59f62e2b",
    "pac_uid": "0_e63870bcecc18",
    "iip": "0",
    "_qimei_uuid42": "183070d3135100ee797b08bc922054dc3062834291",
    "_qimei_fingerprint": "28ec521da86d1fbc149479d2aa40f951",
    "_qimei_q36": "",
    "_qimei_h38": "cb6de4e4797b08bc922054dc02000005818307",
    "pgv_pvid": "1212703189",
    "fqm_pvqid": "50bb40ea-985c-4d11-9cea-7dfefe6ea1ca",
    "_clck": "15sxecs|1|fl1|0",
    "qq_domain_video_guid_verify": "004329d456c0ef18",
    "wr_vid": "346607432",
    "wr_localvid": "6a8327b0814a8cf486a8884",
    "wr_name": "%E6%9C%AC%20%E6%97%A0%20%E9%81%93",
    "wr_gender": "1",
    "wr_rt": "web%40dz_AYa7CIYk07_ucDIb_AL",
    "wr_avatar": "https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FMCpyjIyiaHicBXjh38REzNMA1xXiaeoWJ321CicmRcyMzeSibgDp1z6XC1FVr4szNr4PUsfIqEPRNXa4l9h2NGQsZDg%2F132",
    "wr_fp": "1659424119",
    "wr_pf": "NaN",
    "wr_skey": "ivnZkd2_"
}

# 保留| 默认读三体，其它书籍自行测试时间是否增加
# data = {
#     "appId": "wb182564874663h152492176",
#     "b": "ce032b305a9bc1ce0b0dd2a",
#     "c": "7cb321502467cbbc409e62d",
#     "ci": 70,
#     "co": 0,
#     "sm": "[插图]第三部广播纪元7年，程心艾AA说",
#     "pr": 74,
#     "rt": 30,
#     "ts": 1727660516749,
#     "rn": 31,
#     "sg": "991118cc229871a5442993ecb08b5d2844d7f001dbad9a9bc7b2ecf73dc8db7e",
#     "ct": 1727660516,
#     "ps": "b1d32a307a4c3259g016b67",
#     "pc": "080327b07a4c3259g018787",
# }

# 二十四史
data = {
    'appId': 'wb115321887466h497189850',
    'b': '1d4328e072a6d3131d4e066',
    'c': 'ecc32f3013eccbc87e4b62e',
    'ci': 3,
    'co': 338,
    'sm': '卷一·五帝本纪第一[插图]黄帝者，少典之',
    'pr': 0,
    'rt': 30,
    'ts': 1735441198582,
    'rn': 748,
    'sg': '563b78b53bc54567a31faae31ab07eeb641939a40f5d6796e15acaddc9681b5a',
    'ct': 1735441198,
    'ps': '1aa32e407a5812b4g0164b9',
    'pc': '56b321807a5812b4g01762c',
}


def convert(curl_command):
    """提取headers与cookies"""
    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    cookie_string = headers.pop('cookie', '')
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
