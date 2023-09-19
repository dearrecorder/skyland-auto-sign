import json
import logging

import requests

header = {
    'cred': 'cred',
    'User-Agent': 'Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 31; ) Okhttp/4.11.0',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',

    # 老版本请求头，新版本要验参
    "vName": "1.0.1",
    "vCode": "100001014",
    "dId": "de9759a5afaa634f",
    "platform": "1"
}

header_login = {
    'User-Agent': 'Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 31; ) Okhttp/4.11.0',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',

    # 老版本请求头，新版本要验参
    "vName": "1.0.1",
    "vCode": "100001014",
    "dId": "de9759a5afaa634f",
    "platform": "1"
}

# 签到url
sign_url = "https://zonai.skland.com/api/v1/game/attendance"
# 绑定的角色url
binding_url = "https://zonai.skland.com/api/v1/game/player/binding"

# 使用认证代码获得cred
cred_code_url = "https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code"
# 使用token获得认证代码
grant_code_url = "https://as.hypergryph.com/user/oauth2/v2/grant"

app_code = '4ca99fa6b56cc2ba'


def copy_header(cred):
    v = json.loads(json.dumps(header))
    v['cred'] = cred
    return v


def login_by_token(token_code):
    try:
        t = json.loads(token_code)
        token_code = t['data']['content']
    except:
        pass
    grant_code = get_grant_code(token_code)
    return get_cred(grant_code)


def get_cred(grant):
    resp = requests.post(cred_code_url, json={
        'code': grant,
        'kind': 1
    }, headers=header_login).json()
    if resp['code'] != 0:
        raise Exception(f'获得cred失败：{resp["messgae"]}')
    return resp['data']['cred']


def get_grant_code(token):
    resp = requests.post(grant_code_url, json={
        'appCode': app_code,
        'token': token,
        'type': 0
    }, headers=header_login).json()
    if resp['status'] != 0:
        raise Exception(f'使用token: {token} 获得认证代码失败：{resp["msg"]}')
    return resp['data']['code']


def get_binding_list(cred):
    v = []
    resp = requests.get(url=binding_url, headers=copy_header(cred)).json()
    if resp['code'] != 0:
        logging.error(f"请求角色列表出现问题：{resp['message']}")
        if resp.get('message') == '用户未登录':
            logging.error(f'用户登录可能失效了，请重新登录！')
            return v
    for i in resp['data']['list']:
        if i.get('appCode') != 'arknights':
            continue
        v.extend(i.get('bindingList'))
    return v


def do_sign(cred):
    characters = get_binding_list(cred)
    for i in characters:
        body = {
            'uid': i.get('uid'),
            'gameId': 1
        }
        resp = requests.post(sign_url, headers=copy_header(cred), json=body).json()
        if resp['code'] != 0:
            logging.error(f'角色{i.get("nickName")}({i.get("channelName")})签到失败了！原因：{resp.get("message")}')
            continue
        awards = resp['data']['awards']
        for j in awards:
            res = j['resource']
            logging.info(
                f'角色{i.get("nickName")}({i.get("channelName")})签到成功，获得了{res["name"]}×{res.get("count") or 1}'
            )
