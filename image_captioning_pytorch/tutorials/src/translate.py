import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

with open(os.path.dirname(os.path.abspath(__file__)) + '/../config.json', encoding='utf_8_sig') as j:
    config = json.load(j)

AUTH_KEY = config['auth_key']
DEEPL_TRANSLATE_EP = 'https://api.deepl.com/v2/translate'

def translate(text):
    s_lang=''
    t_lang='JA'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; utf-8'
    }

    params = {
        'auth_key': AUTH_KEY,
        'text': text,
        'target_lang': t_lang
    }

    if s_lang != '':
        params['source_lang'] = s_lang

    req = urllib.request.Request(
        DEEPL_TRANSLATE_EP,
        method='POST',
        data=urllib.parse.urlencode(params).encode('utf-8'),
        headers=headers
    )

    try:
        with urllib.request.urlopen(req) as res:
            res_json = json.loads(res.read().decode('utf-8'))
            s=str(res_json)
            print(s[62:-4])
    except urllib.error.HTTPError as e:
        print(e)
