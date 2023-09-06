import logging
import os.path
import threading

import skyland

# 华为云本地文件在./code下面
# 注：cred过几个小时就会失效，不要使用它，得用鹰角通行证账号获得它
# file_save_name = f'{os.path.dirname(__file__)}/creds.txt'
file_save_token = f'{os.path.dirname(__file__)}/INPUT_HYPERGRYPH_TOKEN.txt'


def read(path):
    v = []
    with open(path, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.strip()
            i and i not in v and v.append(i)
    return v


def handler(event, context):
    token = read(file_save_token)
    if token:
        for i in range(1, len(token)):
            threading.Thread(target=start, args=(token[i],)).start()
        start(token[0])
    return {
        "statusCode": 200,
    }


def start(token):
    try:
        cred = skyland.login_by_token(token)
        skyland.do_sign(cred)
    except Exception as ex:
        logging.error('签到完全失败了！：', exc_info=ex)
